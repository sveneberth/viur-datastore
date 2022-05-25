from viur.datastore.types import KEY_SPECIAL_PROPERTY, DATASTORE_BASE_TYPES, SortOrder, SkelListRef, Entity, \
	QueryDefinition, Key, currentDbAccessLog
from viur.datastore.query import Query
from viur.datastore.utils import fixUnindexableProperties, normalizeKey, keyHelper, IsInTransaction, GetOrInsert, \
	encodeKey, acquireTransactionSuccessMarker, startDataAccessLog, endDataAccessLog
from viur.datastore.transport import Get, Put, Delete, RunInTransaction, AllocateIDs
from viur.datastore.config import conf as config
from viur.datastore.errors import *

import logging
# silencing requests' debugging
logging.getLogger("requests").setLevel(logging.ERROR)
logging.getLogger("urllib3").setLevel(logging.ERROR)


__all__ = [
	"KEY_SPECIAL_PROPERTY",
	"DATASTORE_BASE_TYPES",
	"SortOrder",
	"SkelListRef",
	"Entity",
	"QueryDefinition",
	"Key",
	"Query",
	"fixUnindexableProperties",
	"normalizeKey",
	"keyHelper",
	"Get",
	"Put",
	"Delete",
	"RunInTransaction",
	"IsInTransaction",
	"currentDbAccessLog",
	"GetOrInsert",
	"encodeKey",
	"acquireTransactionSuccessMarker",
	"AllocateIDs",
	"config",
	"startDataAccessLog",
	"endDataAccessLog",
	"ViurDatastoreError",
	"AbortedError",
	"CollisionError",
	"DeadlineExceededError",
	"FailedPreconditionError",
	"InternalError",
	"InvalidArgumentError",
	"NotFoundError",
	"PermissionDeniedError",
	"ResourceExhaustedError",
	"UnauthenticatedError",
	"UnavailableError",
	"NoMutationResultsError",
	"isViurDatastoreRequestOk",
]
