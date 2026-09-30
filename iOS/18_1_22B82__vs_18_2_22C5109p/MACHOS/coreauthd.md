## coreauthd

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/coreauthd`

```diff

-1656.40.25.0.0
-  __TEXT.__text: 0x237b0
+1656.60.119.0.1
+  __TEXT.__text: 0x23e24
   __TEXT.__auth_stubs: 0x770
-  __TEXT.__objc_stubs: 0x32e0
-  __TEXT.__objc_methlist: 0x1028
+  __TEXT.__objc_stubs: 0x3380
+  __TEXT.__objc_methlist: 0xf98
   __TEXT.__const: 0x160
-  __TEXT.__objc_methname: 0x43fc
-  __TEXT.__cstring: 0x25be
-  __TEXT.__objc_classname: 0x6bb
-  __TEXT.__objc_methtype: 0x1eb5
+  __TEXT.__objc_methname: 0x4411
+  __TEXT.__cstring: 0x260a
+  __TEXT.__objc_classname: 0x6a2
+  __TEXT.__objc_methtype: 0x1f44
   __TEXT.__oslogstring: 0x15c6
-  __TEXT.__gcc_except_tab: 0x224
+  __TEXT.__gcc_except_tab: 0x244
   __TEXT.__unwind_info: 0x810
   __DATA_CONST.__auth_got: 0x3c8
-  __DATA_CONST.__got: 0x3d0
+  __DATA_CONST.__got: 0x3f0
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0xa98
-  __DATA_CONST.__cfstring: 0xae0
-  __DATA_CONST.__objc_classlist: 0x108
+  __DATA_CONST.__const: 0xb70
+  __DATA_CONST.__cfstring: 0xac0
+  __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x178
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__objc_superrefs: 0xa8
+  __DATA_CONST.__objc_superrefs: 0x98
   __DATA_CONST.__objc_intobj: 0xd8
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x8320
-  __DATA.__objc_selrefs: 0xf50
-  __DATA.__objc_ivar: 0x184
-  __DATA.__objc_data: 0xa50
+  __DATA.__objc_const: 0x8190
+  __DATA.__objc_selrefs: 0xf60
+  __DATA.__objc_ivar: 0x178
+  __DATA.__objc_data: 0x9b0
   __DATA.__data: 0x11a2
   __DATA.__bss: 0x120
   __DATA.__common: 0x8

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 687
-  Symbols:   255
-  CStrings:  1447
+  Functions: 684
+  Symbols:   259
+  CStrings:  1440
 
Symbols:
+ _OBJC_CLASS_$_LACDTOFeatureEnablementModeCoder
+ _OBJC_CLASS_$_LACDTOKVStoreMigrationController
+ _OBJC_CLASS_$_LACDTOMutableKVStoreReadRequest
+ _OBJC_CLASS_$_LACDTOMutableKVStoreWriteRequest
+ _OBJC_CLASS_$_LACGlobalDomain
- _OBJC_CLASS_$_LACDTOKVStoreGlobalDefaultsDecorator
CStrings:
+ "\x0f\x06"
+ "@\"<LACDTOKVStoreMigrationController>\""
+ "@\"<LACDTOKVStoreReader>\""
+ "@\"LACDTOGracePeriodState\"8@?0"
+ "@\"LACDTOMutableKVStoreReadRequest\"8@?0"
+ "@\"LACDTOMutableKVStoreWriteRequest\"8@?0"
+ "_kvsMigrationController"
+ "_kvstore"
+ "_setValue:forKey:contextUUID:connection:storage:completion:"
+ "_valueForKey:connection:storage:completion:"
+ "bypassEntitlements"
+ "connection"
+ "contextUUID"
+ "decode:"
+ "enableFeatureActivatingGracePeriodWithCompletion:"
+ "initWithContextProvider:kvstore:"
+ "initWithKVStore:defaults:workQueue:"
+ "initWithKVStore:requirementsDataSource:featureFlags:workQueue:"
+ "initWithKey:"
+ "initWithKey:value:"
+ "key"
+ "performMigrationIfNeeded"
+ "processReadRequest:completion:"
+ "processWriteRequest:completion:"
+ "setConnection:"
+ "setContextUUID:"
+ "v24@?0@\"LACDTOKVStoreValue\"8@\"NSError\"16"
+ "v32@0:8@\"<LACDTOKVStoreReadRequest>\"16@?<v@?@\"LACDTOKVStoreValue\"@\"NSError\">24"
+ "v32@0:8@\"<LACDTOKVStoreWriteRequest>\"16@?<v@?@\"NSError\">24"
+ "v64@0:8@16q24@32@40@48@?56"
- "\x0f\x05"
- "\x11"
- "!"
- "<%!@(MISSING) : %!@(MISSING)>"
- "@"
- "@\"<LAContextExternalizationProt>\""
- "@24@0:8q16"
- "@36@0:8i16@20@?28"
- "@?16@0:8"
- "B24@?0@\"OwnerInfo\"8@\"NSDictionary\"16"
- "B32@?0@\"OwnerInfo\"8Q16^B24"
- "OwnerInfo"
- "OwnerInfos"
- "Q20@0:8i16"
- "T@\"<LAContextExternalizationProt>\",R,W,N,V_context"
- "T@\"NSArray\",R,N"
- "T@,R,W,N,V_proxy"
- "T@?,R,N,V_invalidationBlock"
- "Ti,R,N,V_pid"
- "_allInfos"
- "_pid"
- "_proxy"
- "_setValue:forKey:contextUUID:connection:completion:"
- "_storageForKey:"
- "addInfo:"
- "allInfos"
- "context"
- "indexesOfObjectsPassingTest:"
- "initWithContextProvider:"
- "initWithInfo:context:"
- "initWithKVStore:requirementsDataSource:workQueue:"
- "initWithObjects:"
- "initWithProcessId:proxy:invalidationBlock:"
- "invalidationBlock"
- "numberOfOwnersOtherThanPid:"
- "proxy"
- "removeObjectsAtIndexes:"

```
