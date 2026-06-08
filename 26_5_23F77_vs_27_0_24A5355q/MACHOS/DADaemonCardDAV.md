## DADaemonCardDAV

> `/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DACardDAV.framework/DADaemonCardDAV.bundle/DADaemonCardDAV`

```diff

-2691.4.6.0.0
-  __TEXT.__text: 0x26c00
-  __TEXT.__auth_stubs: 0x730
-  __TEXT.__objc_stubs: 0x59c0
-  __TEXT.__objc_methlist: 0x1ee4
-  __TEXT.__const: 0xe0
-  __TEXT.__objc_methname: 0x6b39
-  __TEXT.__oslogstring: 0x3755
-  __TEXT.__objc_classname: 0x609
+2703.0.0.0.0
+  __TEXT.__text: 0x24384
+  __TEXT.__auth_stubs: 0x790
+  __TEXT.__objc_stubs: 0x59e0
+  __TEXT.__objc_methlist: 0x1ed4
+  __TEXT.__const: 0xf0
+  __TEXT.__objc_methname: 0x6b7d
+  __TEXT.__oslogstring: 0x366b
+  __TEXT.__objc_classname: 0x5f4
   __TEXT.__objc_methtype: 0x1619
-  __TEXT.__cstring: 0xa6c
-  __TEXT.__gcc_except_tab: 0x688
-  __TEXT.__unwind_info: 0x6e8
-  __DATA_CONST.__auth_got: 0x3a8
-  __DATA_CONST.__got: 0x4a0
-  __DATA_CONST.__const: 0x6f0
-  __DATA_CONST.__cfstring: 0xa80
+  __TEXT.__cstring: 0xa73
+  __TEXT.__gcc_except_tab: 0x64c
+  __TEXT.__unwind_info: 0x618
+  __DATA_CONST.__const: 0x6c0
+  __DATA_CONST.__cfstring: 0xae0
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__objc_intobj: 0x18
+  __DATA_CONST.__auth_got: 0x3d8
+  __DATA_CONST.__got: 0x4a8
   __DATA.__objc_const: 0x3f80
-  __DATA.__objc_selrefs: 0x1aa8
+  __DATA.__objc_selrefs: 0x1ab0
   __DATA.__objc_ivar: 0x13c
   __DATA.__objc_data: 0xb40
   __DATA.__data: 0x8a0
-  __DATA.__bss: 0xa0
+  __DATA.__bss: 0xb0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/libCTGreenTeaLogger.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 71209AE1-BF3E-30DA-9E43-8F19968BA394
-  Functions: 585
-  Symbols:   364
-  CStrings:  1643
+  UUID: FED31096-9B20-35E5-BB39-112801BCE0C7
+  Functions: 580
+  Symbols:   371
+  CStrings:  1647
 
Symbols:
+ _CardDAVBuildBlacklistFromErrorItems
+ _CardDAVRetryDecisionForHTTPStatus
+ _OBJC_CLASS_$_NSUserDefaults
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "CardDAVDebugForceRetryAfter"
+ "CardDAVDebugForceSyncHTTPStatus"
+ "Container sync task %@ completed and checked for forced status %ld and error %@"
+ "DEBUG: Injecting HTTP %ld on sync task"
+ "Retry-After"
+ "Retrying after %f seconds (lastRetryTimeout=%f, cumulativeRetryTime=%f)"
+ "Unable to obtain authentication account for account \"%{private}@\" %{public}@"
+ "anyBlacklistedItems"
+ "blacklistedHREFs"
+ "blacklistedUUIDs"
+ "cumulativeRetryTime"
+ "dictionaryWithObjects:forKeys:count:"
+ "guardianRestrictedHREFs"
+ "guardianRestrictedUUIDs"
+ "integerForKey:"
+ "setCumulativeRetryTime:"
+ "standardUserDefaults"
+ "stringForKey:"
- "An error item was returned for HREF %{public}@ but we are not blacklisting the associated record. Error: %{public}@ child items: %{public}@"
- "An error item was returned for UUID  %{public}@ but we are not blacklisting the associated record. Error: %{public}@ child items: %{public}@"
- "The server returned a 503, but didn't give us a retry-after header. We'll retry again after %f seconds"
- "The server told us to try again after %f seconds."
- "Unable to obtain authentication account for account \"%@\" %@{public}"
- "_shouldBlacklistForErrorItem:"
- "doubleValue"
- "extraChildItems"
- "guardianRestricted"
- "imageError"
- "invalidImageType"
- "maxImageSize"
- "maxResourceSize"
- "noUIDConflict"
- "v32@?0@\"NSString\"8@\"CoreDAVErrorItem\"16^B24"
- "v32@?0@\"NSURL\"8@\"CoreDAVErrorItem\"16^B24"
- "validAddressData"

```
