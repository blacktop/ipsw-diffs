## biomesyncd

> `/usr/libexec/biomesyncd`

```diff

-209.18.0.0.0
-  __TEXT.__text: 0x4e4e8
-  __TEXT.__auth_stubs: 0xca0
-  __TEXT.__objc_stubs: 0x8820
-  __TEXT.__objc_methlist: 0x3bf4
+236.0.2.0.0
+  __TEXT.__text: 0x4a760
+  __TEXT.__auth_stubs: 0xd00
+  __TEXT.__objc_stubs: 0x8900
+  __TEXT.__objc_methlist: 0x3c24
   __TEXT.__const: 0x1348
-  __TEXT.__gcc_except_tab: 0x9fc
-  __TEXT.__objc_methname: 0xa255
-  __TEXT.__cstring: 0x58e8
-  __TEXT.__objc_classname: 0x83d
-  __TEXT.__objc_methtype: 0x16fe
-  __TEXT.__oslogstring: 0x63bf
-  __TEXT.__unwind_info: 0x1170
-  __DATA_CONST.__auth_got: 0x660
-  __DATA_CONST.__got: 0x3d8
-  __DATA_CONST.__const: 0x10d8
-  __DATA_CONST.__cfstring: 0x46e0
+  __TEXT.__gcc_except_tab: 0x89c
+  __TEXT.__objc_methname: 0xa3f4
+  __TEXT.__cstring: 0x59f8
+  __TEXT.__objc_classname: 0x7f2
+  __TEXT.__objc_methtype: 0x1733
+  __TEXT.__oslogstring: 0x6468
+  __TEXT.__unwind_info: 0x10b0
+  __DATA_CONST.__const: 0x1128
+  __DATA_CONST.__cfstring: 0x4740
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xb0

   __DATA_CONST.__objc_intobj: 0x2e8
   __DATA_CONST.__linkguard: 0xe
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x76f8
-  __DATA.__objc_selrefs: 0x2898
+  __DATA_CONST.__auth_got: 0x690
+  __DATA_CONST.__got: 0x3d8
+  __DATA.__objc_const: 0x7708
+  __DATA.__objc_selrefs: 0x28e0
   __DATA.__objc_ivar: 0x3ec
   __DATA.__objc_data: 0x1180
   __DATA.__data: 0x840

   - /System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets
   - /System/Library/PrivateFrameworks/CloudKitDistributedSync.framework/CloudKitDistributedSync
   - /System/Library/PrivateFrameworks/ContextSync.framework/ContextSync
-  - /System/Library/PrivateFrameworks/IntelligencePlatform.framework/IntelligencePlatform
-  - /System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/IntelligencePlatformLibrary
   - /System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 3A69FAD2-1578-3E86-B4BA-8DB3D36C2F67
-  Functions: 1627
-  Symbols:   343
-  CStrings:  3669
+  UUID: 16CC831D-057B-382B-8F75-664D73F0E0E1
+  Functions: 1625
+  Symbols:   349
+  CStrings:  3691
 
Symbols:
+ _NSClassFromString
+ _OBJC_CLASS_$_BMPersonaUtilities
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x2
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x5
+ _objc_retain_x6
- _OBJC_CLASS_$_GDXPCCoordinationService
CStrings:
+ " with persona: %@"
+ "-[BMSyncServiceServer cascadeCloudKitSyncForSets:reply:]"
+ "-[BMSyncServiceServer cascadeCloudKitSyncWithReply:]"
+ "@\"<BMGDXPCCoordinationService>\""
+ "CCSet"
+ "CascadeRapportWakeSystemDomain"
+ "CascadeRapportWakeUserDomain"
+ "Failed to assume persona %@ with error %@"
+ "GDXPCCoordinationService"
+ "Starting system-domain sync server for event: %s"
+ "Starting user-domain sync server for event: %s%@"
+ "cascadeCloudKitSync called%@"
+ "cascadeCloudKitSyncForSets:reply:"
+ "cascadeCloudKitSyncWithReply:"
+ "cloudKitSyncNowWithReason:activity:sets:dataProtectionClass:completionHandler:"
+ "currentPersonaIdentifierLoggingDescription"
+ "handleIncomingSyncRequestsWithReason:completionHandler:"
+ "handleIncomingSystemDomainSyncRequestsWithReason:completionHandler:"
+ "initializeCloudKitSyncEngine"
+ "runAsPersonaIdentifier:block:"
+ "setClasses:forSelector:argumentIndex:ofReply:"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"NSArray\"@\"NSArray\">24"
- "@\"GDXPCCoordinationService\""
- "CascadeRapportWake"

```
