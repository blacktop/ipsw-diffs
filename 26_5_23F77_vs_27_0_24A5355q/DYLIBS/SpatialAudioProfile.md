## SpatialAudioProfile

> `/System/Library/PrivateFrameworks/SpatialAudioProfile.framework/SpatialAudioProfile`

```diff

-35.14.0.0.0
-  __TEXT.__text: 0xe6c
-  __TEXT.__auth_stubs: 0x1c0
+40.28.1.1.2
+  __TEXT.__text: 0xda8
   __TEXT.__objc_methlist: 0x1ac
   __TEXT.__const: 0x10
   __TEXT.__gcc_except_tab: 0x2c
-  __TEXT.__cstring: 0x332
-  __TEXT.__unwind_info: 0xe0
-  __TEXT.__objc_classname: 0x9d
-  __TEXT.__objc_methname: 0x3de
-  __TEXT.__objc_methtype: 0x119
-  __TEXT.__objc_stubs: 0x2c0
-  __DATA_CONST.__got: 0x38
+  __TEXT.__cstring: 0x336
+  __TEXT.__unwind_info: 0xd8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xa0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20

   __DATA_CONST.__objc_selrefs: 0x110
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xf0
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__cfstring: 0x40
   __AUTH_CONST.__objc_const: 0x340
-  __AUTH.__objc_data: 0xa0
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x20
   __DATA.__data: 0x1f0
+  __DATA_DIRTY.__objc_data: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1A144E39-8A9C-3A63-B64B-1E596935EB43
+  UUID: 04BC7446-6E6E-3E48-AB24-2D5A3E374967
   Functions: 42
-  Symbols:   199
-  CStrings:  94
+  Symbols:   201
+  CStrings:  23
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x1
+ _objc_retain
+ _objc_retain_x2
+ _objc_retain_x8
- _objc_release_x2
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x20
Functions:
~ -[SpatialAudioProfileClient init] : 108 -> 100
~ -[SpatialAudioProfileClient fetchSpatialAudioProfileRecordWithCompletion:] : 160 -> 152
~ ___75-[SpatialAudioProfileClient _fetchSpatialAudioProfileRecordWithCompletion:]_block_invoke : 156 -> 164
~ -[SpatialAudioProfileClient _ensureXPCStarted] : 384 -> 376
~ -[SpatialAudioProfileClient setDispatchQueue:] : 64 -> 12
~ -[SpatialAudioProfileRecord encodeWithCoder:] : 136 -> 128
~ -[SpatialAudioProfileRecord initWithCoder:] : 188 -> 180
~ -[SpatialAudioProfileRecord description] : 116 -> 108
~ -[SpatialAudioProfileRecord setProfileData:] : 64 -> 12
~ -[SpatialAudioProfileRecord setProfileURL:] : 64 -> 12
CStrings:
- ".cxx_destruct"
- "@\"NSData\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSURL\""
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "NSCoding"
- "NSSecureCoding"
- "SpatialAudioProfileRecord"
- "SpatialAudioProfileXPCClientInterface"
- "SpatialAudioProfileXPCServiceInterface"
- "T@\"NSData\",&,N,V_profileData"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_dispatchQueue"
- "T@\"NSURL\",&,N,V_profileURL"
- "T@?,C,N,V_interruptionHandler"
- "T@?,C,N,V_invalidationHandler"
- "TB,R"
- "_dispatchQueue"
- "_ensureXPCStarted"
- "_fetchSpatialAudioProfileRecordWithCompletion:"
- "_interrupted"
- "_interruptionHandler"
- "_invalidateCalled"
- "_invalidateDone"
- "_invalidated"
- "_invalidationHandler"
- "_profileData"
- "_profileURL"
- "_setQueue:"
- "_xpcCnx"
- "decodeObjectOfClass:forKey:"
- "description"
- "dispatchQueue"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "fetchSpatialAudioProfileRecordForClient:WithCompletion:"
- "fetchSpatialAudioProfileRecordWithCompletion:"
- "init"
- "initWithCoder:"
- "initWithServiceName:"
- "interfaceWithProtocol:"
- "interruptionHandler"
- "invalidate"
- "invalidationHandler"
- "profileData"
- "profileURL"
- "remoteObjectProxyWithErrorHandler:"
- "resume"
- "setDispatchQueue:"
- "setExportedInterface:"
- "setExportedObject:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setProfileData:"
- "setProfileURL:"
- "setRemoteObjectInterface:"
- "stringWithFormat:"
- "supportsSecureCoding"
- "v16@0:8"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v32@0:8@\"SpatialAudioProfileClient\"16@?<v@?@\"SpatialAudioProfileRecord\"@\"NSError\">24"
- "v32@0:8@16@?24"

```
