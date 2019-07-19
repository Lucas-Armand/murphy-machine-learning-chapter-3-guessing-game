from django.db import models
import numpy as np
# Create your models here.

class Hypoteses(models.Model):
    name = models.CharField(max_length=200)
    prior = models.FloatField()
    table = models.CharField(max_length=3300)

    def readTable(self):
        str_table = self.table[1:-1]
        list_str_table = str_table.split(",")
        table = [float(value) for value in list_str_table]
        return table

    def likelihood(self,values_list):
        table = self.readTable()
        probabilities = [table[value] for value in values_list]
        likelihood = np.prod(probabilities)
        return likelihood

class NaiveBaysesModel():
    def __init__(self, hypoteses_list=None):
        if hypoteses_list != None:
            self.hypoteses_list = hypoteses_list
        else:
            self.hypoteses_list = Hypoteses.objects.all()

    def priors(self):
        hypoteses = self.hypoteses_list
        priors = []
        for hypotese in hypoteses:
            prior = hypotese.prior
            priors.append(prior)
        hypoteses_names = [h.name for h in hypoteses]
        hypoteses_map = list(zip(priors,hypoteses_names))
        hypoteses_map.sort(key= lambda x : x[0], reverse = True)
        return hypoteses_map

    def posteriors(self, evidences):
        hypoteses = self.hypoteses_list
        Z = 0
        posteriors = []
        for hypotese in hypoteses:
            prior = hypotese.prior
            likelihood = hypotese.likelihood(evidences)
            posterior = prior*likelihood
            Z += posterior
            posteriors.append(posterior)
        Z = sum(posteriors)
        posteriors = [p/Z for p in posteriors]
        hypoteses_map = list(zip(posteriors,hypoteses))
        hypoteses_map.sort(key= lambda x : x[0], reverse = True)
        return hypoteses_map

    def guess(self, evidences):
        posteriors = self.posteriors(evidences)
        best_hypotese = posteriors[0][1]
        prob_table = best_hypotese.readTable()
        last_evidence = max(evidences) # por hipotese a maior e a ultima
        next_evidence_guess = last_evidence
        while True:
            next_evidence_guess +=1
            if next_evidence_guess == 101:
                next_evidence_guess = 0
                break
            if prob_table[next_evidence_guess] > 0:
                break
        return next_evidence_guess
            
