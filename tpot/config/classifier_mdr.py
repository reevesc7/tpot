# -*- coding: utf-8 -*-

"""This file is part of the TPOT library.

TPOT was primarily developed at the University of Pennsylvania by:
    - Randal S. Olson (rso@randalolson.com)
    - Weixuan Fu (weixuanf@upenn.edu)
    - Daniel Angell (dpa34@drexel.edu)
    - and many more generous open source contributors

TPOT is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, either version 3 of
the License, or (at your option) any later version.

TPOT is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with TPOT. If not, see <http://www.gnu.org/licenses/>.

"""

# Check the TPOT documentation for information on the structure of config dicts

tpot_mdr_classifier_config_dict = {

    # Classifiers

    'sklearn.linear_model.LogisticRegression': {
        'penalty': ["l1", "l2"],
        'C': [1e-4, 1e-3, 1e-2, 1e-1, 0.5, 1., 5., 10., 15., 20., 25.],
        'dual': [True, False]
    },

    # Feature constructors

    'mdr.MDR': {
        'tie_break': [0, 1],
        'default_label': [0, 1]
    },

    # Feature Selectors

    'skrebate.ReliefF': {
        'n_features_to_select': [i for i in range(1, 6)],
        'n_neighbors': [2, 10, 50, 100, 250, 500]
    },

    'skrebate.SURF': {
        'n_features_to_select': [i for i in range(1, 6)]
    },

    'skrebate.SURFstar': {
        'n_features_to_select': [i for i in range(1, 6)]
    },

    'skrebate.MultiSURF': {
        'n_features_to_select': [i for i in range(1, 6)]
    }

}
