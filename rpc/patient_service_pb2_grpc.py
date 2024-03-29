# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from rpc import patient_service_pb2 as rpc_dot_patient__service__pb2


class PatientServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.add_patient = channel.unary_unary(
                '/patient.PatientService/add_patient',
                request_serializer=rpc_dot_patient__service__pb2.Patient.SerializeToString,
                response_deserializer=rpc_dot_patient__service__pb2.Patient.FromString,
                )
        self.get_all_patients = channel.unary_stream(
                '/patient.PatientService/get_all_patients',
                request_serializer=rpc_dot_patient__service__pb2.Empty.SerializeToString,
                response_deserializer=rpc_dot_patient__service__pb2.Patient.FromString,
                )
        self.get_patient_by_id = channel.unary_unary(
                '/patient.PatientService/get_patient_by_id',
                request_serializer=rpc_dot_patient__service__pb2.Id.SerializeToString,
                response_deserializer=rpc_dot_patient__service__pb2.Patient.FromString,
                )
        self.update_patient = channel.unary_unary(
                '/patient.PatientService/update_patient',
                request_serializer=rpc_dot_patient__service__pb2.PatientWithId.SerializeToString,
                response_deserializer=rpc_dot_patient__service__pb2.Patient.FromString,
                )


class PatientServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def add_patient(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_all_patients(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_patient_by_id(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update_patient(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PatientServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'add_patient': grpc.unary_unary_rpc_method_handler(
                    servicer.add_patient,
                    request_deserializer=rpc_dot_patient__service__pb2.Patient.FromString,
                    response_serializer=rpc_dot_patient__service__pb2.Patient.SerializeToString,
            ),
            'get_all_patients': grpc.unary_stream_rpc_method_handler(
                    servicer.get_all_patients,
                    request_deserializer=rpc_dot_patient__service__pb2.Empty.FromString,
                    response_serializer=rpc_dot_patient__service__pb2.Patient.SerializeToString,
            ),
            'get_patient_by_id': grpc.unary_unary_rpc_method_handler(
                    servicer.get_patient_by_id,
                    request_deserializer=rpc_dot_patient__service__pb2.Id.FromString,
                    response_serializer=rpc_dot_patient__service__pb2.Patient.SerializeToString,
            ),
            'update_patient': grpc.unary_unary_rpc_method_handler(
                    servicer.update_patient,
                    request_deserializer=rpc_dot_patient__service__pb2.PatientWithId.FromString,
                    response_serializer=rpc_dot_patient__service__pb2.Patient.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'patient.PatientService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PatientService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def add_patient(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/patient.PatientService/add_patient',
            rpc_dot_patient__service__pb2.Patient.SerializeToString,
            rpc_dot_patient__service__pb2.Patient.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_all_patients(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/patient.PatientService/get_all_patients',
            rpc_dot_patient__service__pb2.Empty.SerializeToString,
            rpc_dot_patient__service__pb2.Patient.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_patient_by_id(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/patient.PatientService/get_patient_by_id',
            rpc_dot_patient__service__pb2.Id.SerializeToString,
            rpc_dot_patient__service__pb2.Patient.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def update_patient(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/patient.PatientService/update_patient',
            rpc_dot_patient__service__pb2.PatientWithId.SerializeToString,
            rpc_dot_patient__service__pb2.Patient.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
