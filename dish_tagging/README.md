# Dish tagging
**Author**: Ivan Maksimov (maksimiov.analytics@skoltech.ru, telegram - @Ivan_maksimov)
**Topic**: Multiclass classification with NLP
**Detailed topic description**: Tag dishes based on dish description and receipt
**Methodology**:

- Fit baseline (Multinomial NB)
- Fit word embedding + classification
- Fit Bi-directional LSTM embedding + CNN + classification
- Try pretrained embeddinbgs

**Data**: initially collected from an [open food databese]( https://world.openfoodfacts.org/data). Btw, it is easier to download the same dataset from [this](https://www.kaggle.com/openfoodfacts/world-food-facts) Kaggle dataset

**Target metric**: F1-score with weighted averaging. Weighted - as there is class imbalance

