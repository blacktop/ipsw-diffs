## online-auth-agent

> `/usr/libexec/online-auth-agent`

```diff

-463.100.17.0.0
-  __TEXT.__text: 0x4384c
-  __TEXT.__auth_stubs: 0x1e60
-  __TEXT.__objc_stubs: 0x1f20
+486.0.0.0.0
+  __TEXT.__text: 0x3c768
+  __TEXT.__auth_stubs: 0x1df0
+  __TEXT.__objc_stubs: 0x1c40
   __TEXT.__objc_methlist: 0x7ac
-  __TEXT.__const: 0x246c
-  __TEXT.__cstring: 0x3d96
-  __TEXT.__gcc_except_tab: 0x414
-  __TEXT.__objc_methname: 0x1ed5
-  __TEXT.__oslogstring: 0x399b
+  __TEXT.__const: 0x23fc
+  __TEXT.__cstring: 0x3c06
+  __TEXT.__gcc_except_tab: 0x384
+  __TEXT.__objc_methname: 0x1d25
+  __TEXT.__oslogstring: 0x2d9b
   __TEXT.__objc_classname: 0x358
   __TEXT.__objc_methtype: 0x534
   __TEXT.__dlopen_cstrs: 0x5e

   __TEXT.__constg_swiftt: 0xbfc
   __TEXT.__swift5_builtin: 0x8c
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__swift5_reflstr: 0x785
-  __TEXT.__swift5_fieldmd: 0x9dc
+  __TEXT.__swift5_reflstr: 0x795
+  __TEXT.__swift5_fieldmd: 0x9e8
   __TEXT.__swift5_proto: 0x198
   __TEXT.__swift5_types: 0xf0
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_assocty: 0x168
-  __TEXT.__unwind_info: 0xf88
-  __TEXT.__eh_frame: 0x1360
-  __DATA_CONST.__auth_got: 0xf40
-  __DATA_CONST.__got: 0x4a0
-  __DATA_CONST.__auth_ptr: 0x470
-  __DATA_CONST.__const: 0x2608
-  __DATA_CONST.__cfstring: 0x1540
+  __TEXT.__unwind_info: 0xeb8
+  __TEXT.__eh_frame: 0x1290
+  __DATA_CONST.__const: 0x2440
+  __DATA_CONST.__cfstring: 0x1460
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_intobj: 0x48
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
+  __DATA_CONST.__auth_got: 0xf08
+  __DATA_CONST.__got: 0x450
+  __DATA_CONST.__auth_ptr: 0x468
   __DATA.__objc_const: 0x1420
-  __DATA.__objc_selrefs: 0x970
+  __DATA.__objc_selrefs: 0x8c0
   __DATA.__objc_ivar: 0x60
   __DATA.__objc_data: 0x4c0
   __DATA.__data: 0x16b8
-  __DATA.__bss: 0x3050
+  __DATA.__bss: 0x3030
   __DATA.__common: 0x118
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 40F56BA4-B75A-3B1B-BF7D-A6AD7E830498
-  Functions: 1352
-  Symbols:   445
-  CStrings:  1311
+  UUID: 30B887EF-C08F-3635-9B6C-F5C2F056AF2C
+  Functions: 1260
+  Symbols:   430
+  CStrings:  1196
 
Symbols:
+ _memset
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _swift_release_x1
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x28
+ _swift_release_x8
+ _swift_retain_x1
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x24
+ _swift_retain_x25
+ _swift_retain_x26
+ _swift_retain_x27
+ _swift_retain_x28
+ _swift_retain_x8
- _ASAttributeCompatibilityVersion
- _ASAttributeContentVersion
- _CFAllocatorAllocateTyped
- _CFAllocatorDeallocate
- _CFStringGetCString
- _CFStringGetLength
- _CFStringGetMaximumSizeForEncoding
- _MAIsDownloadResultFailure
- _MAIsQueryResultFailure
- _MAStringForMAAssetState
- _MISBlacklistSetOverride
- _MISQueryBlacklistForBundle
- _MISQueryBlacklistForCdHash
- _OBJC_CLASS_$_LSApplicationProxy
- _OBJC_CLASS_$_MAAsset
- _OBJC_CLASS_$_MAAssetQuery
- _OBJC_CLASS_$_MADownloadOptions
- __CFXPCCreateCFObjectFromXPCObject
- __xpc_event_key_name
- _bsearch_b
- _csops
- _dispatch_async
- _dispatch_queue_attr_make_with_autorelease_frequency
- _dispatch_queue_create
- _dispatch_sync
- _fcopyfile
- _kill
- _lseek
- _malloc_type_malloc
- _mkstemp
- _mmap
- _mprotect
- _munmap
- _objc_initWeak
- _objc_moveWeak
- _proc_listallpids
- _rename
- _strcmp
- _strerror
- _strlcpy
- _swift_unknownObjectRelease_n
- _sysctl
- _unlink
- _xpc_set_event_stream_handler
CStrings:
+ "com.apple.online-auth-agent.launch-warning-sync"
- "Application Installed"
- "Copying asset to temporary ingestion DocCheckList failed, error %{errno}d"
- "Copying asset to temporary ingestion denylist failed, error %{errno}d"
- "Could not allocate buffer for denylist path (this should not happen."
- "Could not initialize key for denylist override."
- "Could not map denylist, error %{errno}d"
- "Could not open denylist, error %{errno}d"
- "Currently installed denylist is broken, replacing unconditionally."
- "Denylist '%s' was issued at %{time_t}lld with %u entries."
- "Denylist asset catalog update failed: %i"
- "Denylist asset query failed: %@"
- "Denylist does not exist."
- "Denylist entries offset %u is past denylist size %lld"
- "Denylist entry number %zu smaller than previous entry: %s < %s"
- "Denylist integrity check failed, not ingesting."
- "Denylist integrity check sentinel not found."
- "Denylist is %td bytes short for entry count"
- "Denylist is too short (%lld bytes) for header (%lu bytes)"
- "Denylist path conversion failed (this should not happen.)"
- "Denylist to ingest is older than current denylist, ignoring."
- "Did not get any user info from event, ignoring."
- "DocCheckList: Failed to chmod 0644 temporary ingestion file '%s': (%d) %s"
- "DocCheckList: Failed to create temporary ingestion file '%s': (%d) %s"
- "DocCheckList: Failed to open new DocCheckList '%s': (%d) %s"
- "DocumentCheckerDefinition.plist.ingestXXXXXXX"
- "Downloaded asset"
- "Downloaded asset failure: %@"
- "Downloaded asset has no path? (This should not happen, update ignored.)"
- "Existing denylist was issued at %lld"
- "Failed rename denylist ingestion file '%s' to actual denylist '%s': (%d) %s"
- "Failed to chmod 0644 temporary ingestion file '%s': (%d) %s"
- "Failed to convert user info XPC dictionary to CF dictionary, ignoring."
- "Failed to create docCheckList ingestion path"
- "Failed to create temporary ingestion file '%s': (%d) %s"
- "Failed to created ingestion path"
- "Failed to mmap fallback denylist header. Giving up."
- "Failed to rename DocCheckList ingestion file '%s' to actual path '%s': (%d) %s"
- "Ingesting DocumentCheckList '%s'"
- "Ingesting denylist '%s'"
- "Latest asset has no path? (This should not happen, update ignored.)"
- "No new denylist found."
- "Opening denylist for ingest failed, not ingesting."
- "Posting DocCheckList notification failed: %d"
- "Relister handling app installation."
- "Relister invoked."
- "Removing potential denylist override for '%@'."
- "Seeing denylist asset '%@' (version '%@', state %ld)"
- "Seen weird bundle ID."
- "Sending denylist to AMFI...."
- "Size mismatch while copying denylist, %ld total, %lld copied."
- "Skipping asset with NULL attributes (this should not happen)."
- "Skipping asset with incompatible compatibility version '%s'."
- "Skipping asset with unparsable content version '%s'."
- "Successfully ingested new DocCheckList '%s'"
- "Successfully ingested new denylist '%s'"
- "The reaper woke up."
- "User info was not a dictionary, ignoring."
- "UserInfo"
- "UserOverriddenCdHashes.plist"
- "Using empty denylist."
- "Using latest asset: %@, state: %ld (%@)"
- "Wrong denylist magic (0x08%x)"
- "applicationProxyForIdentifier:placeholder:"
- "assetId"
- "attributes"
- "auth-list-queue"
- "blacklist-ingest"
- "blov"
- "bundleIDs"
- "bundleURL"
- "cStringUsingEncoding:"
- "cdHash missing from message."
- "com.apple.MobileAsset.MobileIdentityService.DenyList"
- "com.apple.distnoted.matching"
- "com.apple.mis.relister"
- "com.apple.online-auth-agent.denylist-update"
- "com.apple.online-auth-agent.reaper"
- "could not read in auth list (may be non-existing)"
- "creating empty auth list"
- "denylist.map"
- "denylist.map.ingestXXXXXXX"
- "failure writing out auth list"
- "getLocalUrl"
- "haty"
- "i24@?0r^v8r^v16"
- "initWithArray:"
- "initWithContentsOfFile:"
- "initWithType:"
- "online-auth-agent relister"
- "pid space %d*%lu = %lu"
- "queryMetaDataSync"
- "reaper could not get cdhash for pid %d"
- "reaper pid malloc failed."
- "reaper sysctl failed."
- "reaping process %d"
- "removeObject:"
- "results"
- "setAllowsCellularAccess:"
- "setAllowsExpensiveAccess:"
- "setDiscretionary:"
- "setRequiresPowerPluggedIn:"
- "startCatalogDownload:options:then:"
- "startDownload:completionWithError:"
- "state"
- "unsignedLongLongValue"
- "v16@?0q8"
- "v24@?0q8@\"NSError\"16"
- "wasLocal"
- "writeToFile:atomically:"

```
