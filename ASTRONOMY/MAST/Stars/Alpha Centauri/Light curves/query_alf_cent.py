# Import astroquery libraries
from astroquery.mast import Observations

# Define obs (Observation element from astroquery + query_objects asset that admit arguments as object name and search radius)
obs = Observations.query_objects(
  "Proxima Centauri",
  radius = "0.02 deg"
)

# Print obs query results
print(obs)

# Filter the results to get TESS data
tess_obs = obs[obs['obs_collection'] == 'TESS']

# Print the new results the ones that only includes TESS
print(tess_obs)

# Nest products element to tess_obs
products = Observations.get_product_list('tess_obs')

light_curves
