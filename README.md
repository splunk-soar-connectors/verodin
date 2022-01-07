[comment]: # "Auto-generated SOAR connector documentation"
# Verodin

Publisher: Blackstone  
Connector Version: 1\.0\.1  
Product Vendor: Verodin, Inc  
Product Name: Verodin  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 2\.0\.264  

Phantom app for Verodin

### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a Verodin asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**server** |  required  | string | Server IP/Hostname
**username** |  required  | string | API username
**password** |  required  | password | API password
**verify\_server\_cert** |  required  | boolean | Verify server certificate

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity  
[get nodes](#action-get-nodes) - Get node topology  
[get map](#action-get-map) - Get topology map  
[get zone](#action-get-zone) - Get zone\(s\) info  
[delete zone](#action-delete-zone) - Delete a zone  
[get sims actions](#action-get-sims-actions) - Get a list of actions for each simulation  
[run sim](#action-run-sim) - Run a simulation  
[get sim](#action-get-sim) - Get simulation  
[delete sim](#action-delete-sim) - Delete a simulation  
[get job](#action-get-job) - Get information about job\(s\)  
[run\_job](#action-runjob) - Run a job  
[get job actions](#action-get-job-actions) - Get job actions  
[cancel\_job](#action-canceljob) - Cancel a job  

## action: 'test connectivity'
Validate the asset configuration for connectivity

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'get nodes'
Get node topology

Type: **generic**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'get map'
Get topology map

Type: **generic**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'get zone'
Get zone\(s\) info

Type: **generic**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**id** |  optional  | Zone to query | numeric |  `zone id` 

#### Action Output
No Output  

## action: 'delete zone'
Delete a zone

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**id** |  required  | Zone to delete | numeric |  `zone id` 

#### Action Output
No Output  

## action: 'get sims actions'
Get a list of actions for each simulation

Type: **generic**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'run sim'
Run a simulation

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**id** |  required  | Simulation to run | numeric |  `simulation id` 

#### Action Output
No Output  

## action: 'get sim'
Get simulation

Type: **generic**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**id** |  optional  | Simulation to get | numeric |  `simulation id` 
**type** |  optional  | Type of information to get | string |  `simulation type` 

#### Action Output
No Output  

## action: 'delete sim'
Delete a simulation

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**id** |  required  | Simulation to delete | numeric |  `simulation id` 

#### Action Output
No Output  

## action: 'get job'
Get information about job\(s\)

Type: **generic**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**id** |  optional  | Job to query | numeric |  `job id` 

#### Action Output
No Output  

## action: 'run_job'
Run a job

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**id** |  required  | Job to run | numeric |  `job id` 

#### Action Output
No Output  

## action: 'get job actions'
Get job actions

Type: **generic**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**id** |  required  | Job to query | numeric |  `job id` 

#### Action Output
No Output  

## action: 'cancel_job'
Cancel a job

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**id** |  required  | Job to cancel | numeric |  `job id` 

#### Action Output
No Output