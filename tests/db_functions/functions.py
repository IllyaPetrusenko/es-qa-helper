import json
from cassandra import ProtocolVersion
from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster
# from tests.db_functions.json_data.issued_contract import issued_contract


class CassandraSession:
    def __init__(self, cassandra_username, cassandra_password, cassandra_cluster, json_data):
        auth_provider = PlainTextAuthProvider(
            username=cassandra_username,
            password=cassandra_password
        )
        self.cluster = Cluster(
            contact_points=[cassandra_cluster],
            auth_provider=auth_provider,
            protocol_version=ProtocolVersion.V4
        )
        self.contracting_keyspace = self.cluster.connect('contracting')
        self.json_data = json_data

    def insert_contract_ac_status_issued(self, cpid, ocid):
        query = f"""INSERT INTO ac (
        "cpid",
        "ocid",
        "created_date",
        "json_data", 
        "owner", 
        "status", 
        "status_details", 
        "token_entity") VALUES (
        '{cpid}', 
        '{ocid}', 
        '2022-05-18 13:11:29.000+0000', 
        '{json.dumps(self.json_data)}', 
        '445f6851-c908-407d-9b45-14b92f3e964b', 
        'pending', 
        'contractPreparation', 
        '591cd009-258b-4c69-bc18-07e462f9a758');"""
        i = self.contracting_keyspace.execute(query)
        return i

    def insert_contract_po_status_issued(self, cpid, ocid):
        query = f"""INSERT INTO po (
        "cpid",
        "ocid",
        "created_date",
        "json_data", 
        "owner", 
        "status", 
        "status_details", 
        "token_entity") VALUES (
        '{cpid}', 
        '{ocid}', 
        '2022-05-18 13:11:29.000+0000', 
        '{json.dumps(self.json_data)}', 
        '445f6851-c908-407d-9b45-14b92f3e964b', 
        'pending', 
        'contractPreparation', 
        '591cd009-258b-4c69-bc18-07e462f9a758');"""
        i = self.contracting_keyspace.execute(query)
        return i

    def insert_contract_po_status_issued_other_owner(self, cpid, ocid):
        query = f"""INSERT INTO po (
        "cpid",
        "ocid",
        "created_date",
        "json_data", 
        "owner", 
        "status", 
        "status_details", 
        "token_entity") VALUES (
        '{cpid}', 
        '{ocid}', 
        '2022-05-18 13:11:29.000+0000', 
        '{json.dumps(self.json_data)}', 
        '445f6851-c907-407d-9b45-14b92f3e964b', 
        'pending', 
        'contractPreparation', 
        '591cd009-258b-4c69-bc18-07e462f9a758');"""
        i = self.contracting_keyspace.execute(query)
        return i

    def insert_contract_ac_status_issued_other_owner(self, cpid, ocid):
        query = f"""INSERT INTO ac (
        "cpid",
        "ocid",
        "created_date",
        "json_data", 
        "owner", 
        "status", 
        "status_details", 
        "token_entity") VALUES (
        '{cpid}', 
        '{ocid}', 
        '2022-05-18 13:11:29.000+0000', 
        '{json.dumps(self.json_data)}', 
        '445f6851-c908-407d-9b45-14b92f3e964b', 
        'pending', 
        'contractPreparation', 
        '591cd009-258b-4c69-bc28-07e462f9a758');"""
        i = self.contracting_keyspace.execute(query)
        return i

# insert = CassandraSession(
#     cassandra_username='caclient',
#     cassandra_password='6AH7vbrkMWnfK',
#     cassandra_cluster='10.0.20.106',
#     json_data=issued_contract
# )
# a = insert.insert_contract_status_issued()
# print(a)
