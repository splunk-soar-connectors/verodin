# Verodin status codes
STATUS_CODES = {
    200: 'Request completed successfully.',
    201: 'Create request completed successfully.',
    400: 'Request error. See response body for details.',
    401: 'Authentication failure, invalid access credentials.',
    403: 'Insufficient permissions.',
    404: 'Requested URI does not exist.',
    409: 'Invalid operation.',
    500: 'Unspecified internal server error.',
    503: 'Feature is disabled in configuration file.'
}

# Verodin API calls
TOPOLOGY_NODES = '/topology/nodes.json'
TOPOLOGY_MAP = '/topology/map.json'
SECURITY_ZONES = '/security_zones.json'
SECURITY_ZONE = '/security_zones/{zone_id}.json'
SIMS_ACTIONS = '/manage_sims/actions.json'
RUN_ACTIONS = '/manage_sims/actions/{action_id}/run.json'
SIMS_SEQUENCE = '/simulations.json?sim_type=sequence'
SIMS_EVAL = '/simulations.json?sim_type=eval'
SIM = '/simulations/{sim_id}.json'
JOBS = '/jobs.json'
JOB = '/jobs/{job_id}.json'
RERUN_JOB = '/jobs/{job_id}/run_again.json'
JOB_ACTIONS = '/jobs/{job_id}/sim_actions.json'
CANCEL_JOB = '/jobs/{job_id}/cancel.json'

# Phantom actions
ACTION_ID_GET_NODES = 'get_nodes'
ACTION_ID_GET_MAP = 'get_map'
ACTION_ID_GET_ZONE = 'get_zone'
ACTION_ID_DELETE_ZONE = 'delete_zone'
ACTION_ID_GET_SIMS_ACTIONS = 'get_sims_actions'
ACTION_ID_RUN_SIM = 'run_sim'
ACTION_ID_GET_SIM = 'get_sim'
ACTION_ID_DELETE_SIM = 'delete_sim'
ACTION_ID_GET_JOB = 'get_job'
ACTION_ID_RUN_JOB = 'run_job'
ACTION_ID_GET_JOB_ACTIONS = 'get_job_actions'
ACTION_ID_CANCEL_JOB = 'cancel_job'
