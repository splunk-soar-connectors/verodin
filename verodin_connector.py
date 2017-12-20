# I dislike the print statement
from __future__ import print_function

# Phantom imports
import phantom.app as phantom
from phantom.app import BaseConnector
from phantom.app import ActionResult

import requests

from verodin_consts import *


class VerodinConnector(BaseConnector):
    def __init__(self):
        # Must call the BaseConnectors init first
        super(VerodinConnector, self).__init__()

    def _test_connectivity(self, param):
        # Get the config
        config = self.get_config()

        self.debug_print('param', param)

        self.save_progress("Querying Verodin server to check connectivity")

        # Progress
        self.save_progress(phantom.APP_PROG_CONNECTING_TO_ELLIPSES, config['server'])

        try:
            resp = requests.get('https://' + config['server'], verify=config[phantom.APP_JSON_VERIFY])
            resp.raise_for_status()
        except requests.HTTPError as e:
            self.set_status(phantom.APP_ERROR, 'Unable to connect to server', e)
            return self.get_status()

        return self.set_status_save_progress(phantom.APP_SUCCESS, 'Connection successful')

    def _handle_get_nodes(self):
        # Get the config
        config = self.get_config()

        # Add an action result to the App Run
        action_result = ActionResult()
        self.add_action_result(action_result)

        url = 'https://' + config['server'] + TOPOLOGY_NODES

        try:
            self.save_progress('Using URL ' + url, verify=config[phantom.APP_JSON_VERIFY])
            resp = requests.get(url, auth=(config['username'], config['password']), verify=config[phantom.APP_JSON_VERIFY])
            resp.raise_for_status()
            action_result.set_status(phantom.APP_SUCCESS)
        except requests.HTTPError as e:
            action_result.set_status(phantom.APP_ERROR, 'Unable to get nodes', e)
            return action_result.get_status()

        action_result.add_data(resp.json())

        return action_result.get_status()

    def _handle_get_map(self):
        # Get the config
        config = self.get_config()

        # Add an action result to the App Run
        action_result = ActionResult()
        self.add_action_result(action_result)

        url = 'https://' + config['server'] + TOPOLOGY_MAP

        try:
            self.save_progress('Using URL ' + url, verify=config[phantom.APP_JSON_VERIFY])
            resp = requests.get(url, auth=(config['username'], config['password']), verify=config[phantom.APP_JSON_VERIFY])
            resp.raise_for_status()
            action_result.set_status(phantom.APP_SUCCESS)
        except requests.HTTPError as e:
            action_result.set_status(phantom.APP_ERROR, 'Unable to get map', e)
            return action_result.get_status()

        action_result.add_data(resp.json())

        return action_result.get_status()

    def _handle_get_zone(self, param):
        # Get the config
        config = self.get_config()

        self.debug_print('param', param)

        # Add an action result to the App Run
        action_result = ActionResult(dict(param))
        self.add_action_result(action_result)

        # Get the zone ID (if any)
        zone_id = param.get('id')

        if zone_id:
            url = 'https://' + config['server'] + SECURITY_ZONE.format(zone_id=zone_id)
        else:
            url = 'https://' + config['server'] + SECURITY_ZONES

        try:
            self.save_progress('Using URL ' + url, verify=config[phantom.APP_JSON_VERIFY])
            resp = requests.get(url, auth=(config['username'], config['password']), verify=config[phantom.APP_JSON_VERIFY])
            resp.raise_for_status()
            action_result.set_status(phantom.APP_SUCCESS)
        except requests.HTTPError as e:
            action_result.set_status(phantom.APP_ERROR, 'Unable to get zone(s)', e)
            return action_result.get_status()

        action_result.add_data(resp.json())

        return action_result.get_status()

    def _handle_delete_zone(self, param):
        # Get the config
        config = self.get_config()

        self.debug_print('param', param)

        # Add an action result to the App Run
        action_result = ActionResult(dict(param))
        self.add_action_result(action_result)

        # Get the zone ID
        zone_id = param.get('id')

        url = 'https://' + config['server'] + SECURITY_ZONE.format(zone_id=zone_id)

        try:
            self.save_progress('Using URL ' + url, verify=config[phantom.APP_JSON_VERIFY])
            resp = requests.delete(url, auth=(config['username'], config['password']), verify=config[phantom.APP_JSON_VERIFY])
            resp.raise_for_status()
            action_result.set_status(phantom.APP_SUCCESS)
        except requests.HTTPError as e:
            action_result.set_status(phantom.APP_ERROR, 'Unable to delete zone', e)
            return action_result.get_status()

        return action_result.get_status()

    def _handle_get_sims_actions(self):
        # Get the config
        config = self.get_config()

        # Add an action result to the App Run
        action_result = ActionResult()
        self.add_action_result(action_result)

        url = 'https://' + config['server'] + SIMS_ACTIONS

        try:
            self.save_progress('Using URL ' + url, verify=config[phantom.APP_JSON_VERIFY])
            resp = requests.get(url, auth=(config['username'], config['password']), verify=config[phantom.APP_JSON_VERIFY])
            resp.raise_for_status()
            action_result.set_status(phantom.APP_SUCCESS)
        except requests.HTTPError as e:
            action_result.set_status(phantom.APP_ERROR, 'Unable to get simulations actions', e)
            return action_result.get_status()

        action_result.add_data(resp.json())

        return action_result.get_status()

    def _handle_run_sim(self, param):
        # Get the config
        config = self.get_config()

        self.debug_print('param', param)

        # Add an action result to the App Run
        action_result = ActionResult(dict(param))
        self.add_action_result(action_result)

        # Get the simulation ID
        action_id = param.get('id')

        url = 'https://' + config['server'] + RUN_ACTIONS.format(action_id=action_id)

        try:
            self.save_progress('Using URL ' + url, verify=config[phantom.APP_JSON_VERIFY])
            resp = requests.get(url, auth=(config['username'], config['password']), verify=config[phantom.APP_JSON_VERIFY])
            resp.raise_for_status()
            action_result.set_status(phantom.APP_SUCCESS)
        except requests.HTTPError as e:
            action_result.set_status(phantom.APP_ERROR, 'Unable to run simulation action', e)
            return action_result.get_status()

        action_result.add_data(resp.json())

        return action_result.get_status()

    def _handle_get_sim(self, param):
        # Get the config
        config = self.get_config()

        self.debug_print('param', param)

        # Add an action result to the App Run
        action_result = ActionResult(dict(param))
        self.add_action_result(action_result)

        # Get the simulation ID or type
        sim_id = param.get('id')
        sim_type = param.get('type')

        if sim_id:
            url = 'https://' + config['server'] + SIM.format(sim_id=sim_id)
        elif sim_type == 'sequence':
            url = 'https://' + config['server'] + SIMS_SEQUENCE
        else:
            url = 'https://' + config['server'] + SIMS_EVAL

        try:
            self.save_progress('Using URL ' + url, verify=config[phantom.APP_JSON_VERIFY])
            resp = requests.get(url, auth=(config['username'], config['password']), verify=config[phantom.APP_JSON_VERIFY])
            resp.raise_for_status()
            action_result.set_status(phantom.APP_SUCCESS)
        except requests.HTTPError as e:
            action_result.set_status(phantom.APP_ERROR, 'Unable to get simulation(s)', e)
            return action_result.get_status()

        action_result.add_data(resp.json())

        return action_result.get_status()

    def _handle_delete_sim(self, param):
        # Get the config
        config = self.get_config()

        self.debug_print('param', param)

        # Add an action result to the App Run
        action_result = ActionResult(dict(param))
        self.add_action_result(action_result)

        # Get the simulation ID
        sim_id = param.get('id')

        url = 'https://' + config['server'] + SIM.format(sim_id=sim_id)

        try:
            self.save_progress('Using URL ' + url, verify=config[phantom.APP_JSON_VERIFY])
            resp = requests.delete(url, auth=(config['username'], config['password']), verify=config[phantom.APP_JSON_VERIFY])
            resp.raise_for_status()
            action_result.set_status(phantom.APP_SUCCESS)
        except requests.HTTPError as e:
            action_result.set_status(phantom.APP_ERROR, 'Unable to delete simulation', e)
            return action_result.get_status()

        return action_result.get_status()

    def _handle_get_job(self, param):
        # Get the config
        config = self.get_config()

        self.debug_print('param', param)

        # Add an action result to the App Run
        action_result = ActionResult(dict(param))
        self.add_action_result(action_result)

        # Get the job ID (if any)
        job_id = param.get('id')

        if job_id:
            url = 'https://' + config['server'] + JOB.format(job_id=job_id)
        else:
            url = 'https://' + config['server'] + JOBS

        try:
            self.save_progress('Using URL ' + url, verify=config[phantom.APP_JSON_VERIFY])
            resp = requests.get(url, auth=(config['username'], config['password']), verify=config[phantom.APP_JSON_VERIFY])
            resp.raise_for_status()
            action_result.set_status(phantom.APP_SUCCESS)
        except requests.HTTPError as e:
            action_result.set_status(phantom.APP_ERROR, 'Unable to get job(s)', e)
            return action_result.get_status()

        action_result.add_data(resp.json())

        return action_result.get_status()

    def _handle_run_job(self, param):
        # Get the config
        config = self.get_config()

        self.debug_print('param', param)

        # Add an action result to the App Run
        action_result = ActionResult(dict(param))
        self.add_action_result(action_result)

        # Get the job ID
        job_id = param.get('id')

        url = 'https://' + config['server'] + RERUN_JOB.format(job_id=job_id)

        try:
            self.save_progress('Using URL ' + url, verify=config[phantom.APP_JSON_VERIFY])
            resp = requests.get(url, auth=(config['username'], config['password']), verify=config[phantom.APP_JSON_VERIFY])
            resp.raise_for_status()
            action_result.set_status(phantom.APP_SUCCESS)
        except requests.HTTPError as e:
            action_result.set_status(phantom.APP_ERROR, 'Unable to run job', e)
            return action_result.get_status()

        action_result.add_data(resp.json())

        return action_result.get_status()

    def _handle_get_job_actions(self, param):
        # Get the config
        config = self.get_config()

        self.debug_print('param', param)

        # Add an action result to the App Run
        action_result = ActionResult(dict(param))
        self.add_action_result(action_result)

        # Get the job ID
        job_id = param.get('id')

        url = 'https://' + config['server'] + JOB_ACTIONS.format(job_id=job_id)

        try:
            self.save_progress('Using URL ' + url, verify=config[phantom.APP_JSON_VERIFY])
            resp = requests.get(url, auth=(config['username'], config['password']), verify=config[phantom.APP_JSON_VERIFY])
            resp.raise_for_status()
            action_result.set_status(phantom.APP_SUCCESS)
        except requests.HTTPError as e:
            action_result.set_status(phantom.APP_ERROR, 'Unable to get actions for job', e)
            return action_result.get_status()

        action_result.add_data(resp.json())

        return action_result.get_status()

    def _handle_cancel_job(self, param):
        # Get the config
        config = self.get_config()

        self.debug_print('param', param)

        # Add an action result to the App Run
        action_result = ActionResult(dict(param))
        self.add_action_result(action_result)

        # Get the job ID
        job_id = param.get('id')

        url = 'https://' + config['server'] + CANCEL_JOB.format(job_id=job_id)

        try:
            self.save_progress('Using URL ' + url, verify=config[phantom.APP_JSON_VERIFY])
            resp = requests.get(url, auth=(config['username'], config['password']), verify=config[phantom.APP_JSON_VERIFY])
            resp.raise_for_status()
            action_result.set_status(phantom.APP_SUCCESS)
        except requests.HTTPError as e:
            action_result.set_status(phantom.APP_ERROR, 'Unable to cancel job', e)
            return action_result.get_status()

        action_result.add_data(resp.json())

        return action_result.get_status()

    def handle_action(self, param):
        ret_val = phantom.APP_SUCCESS

        # Get the action that we are supposed to execute
        action_id = self.get_action_identifier()

        self.debug_print('action_id', action_id)

        if action_id == phantom.ACTION_ID_TEST_ASSET_CONNECTIVITY:
            ret_val = self._test_connectivity(param)
        elif action_id == ACTION_ID_GET_NODES:
            ret_val = self._handle_get_nodes()
        elif action_id == ACTION_ID_GET_MAP:
            ret_val = self._handle_get_map()
        elif action_id == ACTION_ID_GET_ZONE:
            ret_val = self._handle_get_zone(param)
        elif action_id == ACTION_ID_DELETE_ZONE:
            ret_val = self._handle_delete_zone(param)
        elif action_id == ACTION_ID_GET_SIMS_ACTIONS:
            ret_val = self._handle_get_sims_actions()
        elif action_id == ACTION_ID_RUN_SIM:
            ret_val = self._handle_run_sim(param)
        elif action_id == ACTION_ID_GET_SIM:
            ret_val = self._handle_get_sim(param)
        elif action_id == ACTION_ID_DELETE_SIM:
            ret_val = self._handle_delete_sim(param)
        elif action_id == ACTION_ID_GET_JOB:
            ret_val = self._handle_get_job(param)
        elif action_id == ACTION_ID_RUN_JOB:
            ret_val = self._handle_run_job(param)
        elif action_id == ACTION_ID_GET_JOB_ACTIONS:
            ret_val = self._handle_get_job_actions(param)
        elif action_id == ACTION_ID_CANCEL_JOB:
            ret_val = self._handle_cancel_job(param)

        return ret_val


if __name__ == '__main__':
    import json
    import sys

    if len(sys.argv) < 2:
        print('No test json specified as input')
        exit(0)

    with open(sys.argv[1]) as f:
        in_json = f.read()
        in_json = json.loads(in_json)
        print(json.dumps(in_json, indent=4))

        connector = VerodinConnector()
        connector.print_progress_message = True
        ret_val = connector._handle_action(json.dumps(in_json), None)
        print(json.dumps(json.loads(ret_val), indent=4))
