### Пропущенные значения
---
```python
# Визуализация. Определяем цвета: желтый - данные заполнены, синий - пропущенные
cols = df.columns[:35]
colours = ['#000099', '#ffff00']
sns.heatmap(df[cols].isnull(), cmap=sns.color_palette(colours))
```
