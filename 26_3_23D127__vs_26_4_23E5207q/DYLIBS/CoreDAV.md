## CoreDAV

> `/System/Library/PrivateFrameworks/CoreDAV.framework/CoreDAV`

```diff

-1236.2.1.0.0
-  __TEXT.__text: 0x521b8
-  __TEXT.__auth_stubs: 0xa60
-  __TEXT.__objc_methlist: 0x56e0
+1236.4.5.0.0
+  __TEXT.__text: 0x58294
+  __TEXT.__auth_stubs: 0xa00
+  __TEXT.__objc_methlist: 0x56f8
   __TEXT.__cstring: 0x3d21
   __TEXT.__const: 0xe0
   __TEXT.__oslogstring: 0x4402
-  __TEXT.__gcc_except_tab: 0x810
-  __TEXT.__unwind_info: 0xf58
-  __TEXT.__objc_classname: 0xd42
-  __TEXT.__objc_methname: 0xbc30
-  __TEXT.__objc_methtype: 0x19e9
-  __TEXT.__objc_stubs: 0x7640
+  __TEXT.__gcc_except_tab: 0x668
+  __TEXT.__unwind_info: 0x1570
+  __TEXT.__objc_classname: 0xd41
+  __TEXT.__objc_methname: 0xbcaf
+  __TEXT.__objc_methtype: 0x1a34
+  __TEXT.__objc_stubs: 0x7660
   __DATA_CONST.__got: 0x498
-  __DATA_CONST.__const: 0xf78
+  __DATA_CONST.__const: 0xf70
   __DATA_CONST.__objc_classlist: 0x378
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2780
+  __DATA_CONST.__objc_selrefs: 0x2790
   __DATA_CONST.__objc_superrefs: 0x358
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x540
+  __AUTH_CONST.__auth_got: 0x510
   __AUTH_CONST.__const: 0x240
   __AUTH_CONST.__cfstring: 0x5c20
-  __AUTH_CONST.__objc_const: 0xadd0
+  __AUTH_CONST.__objc_const: 0xaed8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x794

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 535044FB-197D-301C-AABE-96CEA411B887
-  Functions: 1711
-  Symbols:   6459
-  CStrings:  4105
+  UUID: 21DD529D-D097-3D00-90AA-FDCB693C50C6
+  Functions: 1720
+  Symbols:   6464
+  CStrings:  4112
 
Symbols:
+ -[CoreDAVSyncReportTask getPreviousSyncToken]
+ _OBJC_IVAR_$_CoreDAVDiscoveryAccountInfo._accountID
+ _OBJC_IVAR_$_CoreDAVDiscoveryAccountInfo._backingAccountInfoProvider
+ _OBJC_IVAR_$_CoreDAVDiscoveryAccountInfo._error
+ _OBJC_IVAR_$_CoreDAVDiscoveryAccountInfo._host
+ _OBJC_IVAR_$_CoreDAVDiscoveryAccountInfo._identityPersist
+ _OBJC_IVAR_$_CoreDAVDiscoveryAccountInfo._password
+ _OBJC_IVAR_$_CoreDAVDiscoveryAccountInfo._port
+ _OBJC_IVAR_$_CoreDAVDiscoveryAccountInfo._principalURL
+ _OBJC_IVAR_$_CoreDAVDiscoveryAccountInfo._scheme
+ _OBJC_IVAR_$_CoreDAVDiscoveryAccountInfo._serverComplianceClasses
+ _OBJC_IVAR_$_CoreDAVDiscoveryAccountInfo._serverHeaders
+ _OBJC_IVAR_$_CoreDAVDiscoveryAccountInfo._serverRoot
+ _OBJC_IVAR_$_CoreDAVDiscoveryAccountInfo._shouldFailAllTasks
+ _OBJC_IVAR_$_CoreDAVDiscoveryAccountInfo._started
+ _OBJC_IVAR_$_CoreDAVDiscoveryAccountInfo._success
+ _OBJC_IVAR_$_CoreDAVDiscoveryAccountInfo._user
+ _OBJC_IVAR_$_CoreDAVDiscoveryAccountInfo._userAgentHeader
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ ___43-[CoreDAVDiscoveryTaskGroup startTaskGroup]_block_invoke.299
+ ___53-[CoreDAVDiscoveryTaskGroup completeDiscovery:error:]_block_invoke.311
+ ___53-[CoreDAVDiscoveryTaskGroup completeDiscovery:error:]_block_invoke.312
+ ___53-[CoreDAVDiscoveryTaskGroup completeDiscovery:error:]_block_invoke.316
+ ___53-[CoreDAVDiscoveryTaskGroup completeDiscovery:error:]_block_invoke.320
+ ___53-[CoreDAVDiscoveryTaskGroup completeDiscovery:error:]_block_invoke.327
+ ___53-[CoreDAVDiscoveryTaskGroup completeDiscovery:error:]_block_invoke.328
+ _objc_msgSend$completeWithError:httpMethod:latency:task:responseStatusCode:
- OBJC_IVAR_$_CoreDAVDiscoveryAccountInfo._accountID
- OBJC_IVAR_$_CoreDAVDiscoveryAccountInfo._backingAccountInfoProvider
- OBJC_IVAR_$_CoreDAVDiscoveryAccountInfo._error
- OBJC_IVAR_$_CoreDAVDiscoveryAccountInfo._host
- OBJC_IVAR_$_CoreDAVDiscoveryAccountInfo._identityPersist
- OBJC_IVAR_$_CoreDAVDiscoveryAccountInfo._password
- OBJC_IVAR_$_CoreDAVDiscoveryAccountInfo._port
- OBJC_IVAR_$_CoreDAVDiscoveryAccountInfo._principalURL
- OBJC_IVAR_$_CoreDAVDiscoveryAccountInfo._scheme
- OBJC_IVAR_$_CoreDAVDiscoveryAccountInfo._serverComplianceClasses
- OBJC_IVAR_$_CoreDAVDiscoveryAccountInfo._serverHeaders
- OBJC_IVAR_$_CoreDAVDiscoveryAccountInfo._serverRoot
- OBJC_IVAR_$_CoreDAVDiscoveryAccountInfo._shouldFailAllTasks
- OBJC_IVAR_$_CoreDAVDiscoveryAccountInfo._started
- OBJC_IVAR_$_CoreDAVDiscoveryAccountInfo._success
- OBJC_IVAR_$_CoreDAVDiscoveryAccountInfo._user
- OBJC_IVAR_$_CoreDAVDiscoveryAccountInfo._userAgentHeader
- ___43-[CoreDAVDiscoveryTaskGroup startTaskGroup]_block_invoke.286
- ___53-[CoreDAVDiscoveryTaskGroup completeDiscovery:error:]_block_invoke.298
- ___53-[CoreDAVDiscoveryTaskGroup completeDiscovery:error:]_block_invoke.299
- ___53-[CoreDAVDiscoveryTaskGroup completeDiscovery:error:]_block_invoke.303
- ___53-[CoreDAVDiscoveryTaskGroup completeDiscovery:error:]_block_invoke.307
- ___53-[CoreDAVDiscoveryTaskGroup completeDiscovery:error:]_block_invoke.314
- ___53-[CoreDAVDiscoveryTaskGroup completeDiscovery:error:]_block_invoke.315
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x7
CStrings:
+ "T@\"NSString\",?,R,C,N"
+ "T@\"NSURL\",R,N"
+ "TB,?,R,N"
+ "completeWithError:httpMethod:latency:task:responseStatusCode:"
+ "getPreviousSyncToken"
+ "v56@0:8@\"NSError\"16@\"NSString\"24d32@\"NSString\"40q48"
+ "v56@0:8@16@24d32@40q48"

```
