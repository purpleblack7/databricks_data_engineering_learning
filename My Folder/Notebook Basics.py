# Databricks notebook source
print("Hello World")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT "Hello World From SQL"

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Well hello there
# MAGIC
# MAGIC * Bullet point
# MAGIC   * Bullet Point 1
# MAGIC

# COMMAND ----------

# MAGIC %run ../includes/Setup

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %fs
# MAGIC ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

files = dbutils.fs.ls('/databricks-datasets')
print(files)

# COMMAND ----------

display(files)

# COMMAND ----------


