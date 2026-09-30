## nfsd

> `/sbin/nfsd`

```diff

-316.80.1.0.0
-  __TEXT.__text: 0xf580
-  __TEXT.__auth_stubs: 0xb40
-  __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0x4435
-  __TEXT.__unwind_info: 0x1e8
-  __DATA_CONST.__auth_got: 0x5a0
-  __DATA_CONST.__got: 0x80
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x198
+327.100.3.0.0
+  __TEXT.__text: 0xe794
+  __TEXT.__auth_stubs: 0xa50
+  __TEXT.__const: 0x90
+  __TEXT.__cstring: 0x3d32
+  __TEXT.__unwind_info: 0x1b8
+  __DATA_CONST.__auth_got: 0x528
+  __DATA_CONST.__got: 0x68
+  __DATA_CONST.__auth_ptr: 0x10
+  __DATA_CONST.__const: 0xd8
   __DATA_CONST.__cfstring: 0xc0
-  __DATA.__data: 0x60c
-  __DATA.__common: 0x630
-  __DATA.__bss: 0x610
+  __DATA.__data: 0x66
+  __DATA.__common: 0x628
+  __DATA.__bss: 0x428
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/DiskArbitration.framework/Versions/A/DiskArbitration
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /System/Library/PrivateFrameworks/oncrpc.framework/Versions/A/oncrpc
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: EE8F84BA-D4DF-30C4-87FE-6F005314C836
-  Functions: 124
-  Symbols:   199
-  CStrings:  670
+  UUID: 6EB1A376-E963-3C38-9709-E06C6979ADCC
+  Functions: 112
+  Symbols:   181
+  CStrings:  567
 
Symbols:
- __NSConcreteGlobalBlock
- __NSConcreteStackBlock
- __dispatch_source_type_timer
- __newrpclib_netid2socparms
- __newrpclib_svc_getnetid
- _analytics_send_event_lazy
- _dispatch_resume
- _dispatch_source_cancel
- _dispatch_source_create
- _dispatch_source_set_event_handler
- _dispatch_source_set_timer
- _getenv
- _memcmp
- _xpc_dictionary_create_empty
- _xpc_dictionary_set_bool
- _xpc_dictionary_set_int64
- _xpc_dictionary_set_string
- _xpc_dictionary_set_uint64
CStrings:
- "%s %llu"
- "%s %llu\n"
- "%s: Failed to open the file"
- "%s: Incorrect key: got <%s>, expected <%s>"
- "/var/run/nfs.stats"
- "32BITCLIENTS"
- "ACCESS"
- "AF_INET"
- "AF_INET6"
- "AF_LOCAL"
- "ALLDIRS"
- "COMMIT"
- "CREATE"
- "FSINFO"
- "FSPATH"
- "FSSTAT"
- "FSUUID"
- "GETATTR"
- "HOST_COUNT"
- "HOST_COUNT_LOOPBACK"
- "LINK"
- "LOOKUP"
- "MANGLEDNAMES"
- "MAPALL"
- "MAPROOT"
- "MASK"
- "MKDIR"
- "MKNOD"
- "NET"
- "NFS_Version"
- "NFSv2"
- "NFSv3"
- "NULL"
- "OFFLINE"
- "PATHCONF"
- "READ"
- "READDIR"
- "READDIRPLUS"
- "READLINK"
- "READONLY"
- "REMOVE"
- "RENAME"
- "RMDIR"
- "SECFLAV"
- "SETATTR"
- "SOCK_DGRAM"
- "SOCK_RAW"
- "SOCK_STREAM"
- "SRVCACHE_IDEMONE_HITS"
- "SRVCACHE_INPROG_HITS"
- "SRVCACHE_MISSES"
- "SRVCACHE_NON_IDEMONE_HITS"
- "SRVWRITE_Opsaved"
- "SRVWRITE_WriteOps"
- "SRVWRITE_WriteRPC"
- "SVC_ERRS"
- "SVC_RPC_ERRS"
- "SYMLINK"
- "Socket_Family"
- "Socket_Type"
- "Unknown"
- "WRITE"
- "XCTestSessionIdentifier"
- "^v8@?0"
- "async"
- "bonjour"
- "bonjour_local_domain_only"
- "com.apple.nfs.server.config"
- "com.apple.nfs.server.exports"
- "com.apple.nfs.server.mount"
- "com.apple.nfs.server.statistics"
- "export_hash_size"
- "fsevents"
- "m"
- "materialize_dataless_files"
- "mount_port"
- "mount_regular_files"
- "mount_require_resv_port"
- "n"
- "nfsd_analytics:com.apple.nfs.server.config invalid netid"
- "nfsd_analytics:com.apple.nfs.server.config invalid out type"
- "nfsd_analytics:com.apple.nfs.server.config netid2socparms failure"
- "nfsd_analytics:com.apple.nfs.server.config sending event"
- "nfsd_analytics:com.apple.nfs.server.exports sending event"
- "nfsd_analytics:com.apple.nfs.server.mount sending event"
- "nfsd_analytics:com.apple.nfs.server.statistics failure %d"
- "nfsd_analytics:com.apple.nfs.server.statistics kernel statistics were zeroed"
- "nfsd_analytics:com.apple.nfs.server.statistics sending event"
- "nfsd_analytics:com.apple.nfs.server.statistics statistics were not changed "
- "nfsd_analytics_event_statistics_read_file"
- "nfsd_analytics_event_statistics_write_file"
- "nfsd_threads"
- "o"
- "port"
- "reqcache_size"
- "request_queue_length"
- "require_resv_port"
- "ro"
- "up"
- "user_stats"
- "v8@?0"
- "wg_delay"
- "wg_delay_v3"

```
