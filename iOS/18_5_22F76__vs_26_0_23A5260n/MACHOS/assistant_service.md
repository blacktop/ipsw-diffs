## assistant_service

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistant_service`

```diff

-3405.29.4.11.2
-  __TEXT.__text: 0x9e10
-  __TEXT.__auth_stubs: 0x600
-  __TEXT.__objc_stubs: 0x15e0
-  __TEXT.__objc_methlist: 0xaac
+3500.97.4.1.2
+  __TEXT.__text: 0x94ec
+  __TEXT.__auth_stubs: 0x610
+  __TEXT.__objc_stubs: 0x1560
+  __TEXT.__objc_methlist: 0xa84
   __TEXT.__const: 0x48
   __TEXT.__gcc_except_tab: 0xb8
-  __TEXT.__cstring: 0x14fd
-  __TEXT.__oslogstring: 0xdab
-  __TEXT.__objc_methname: 0x19e1
+  __TEXT.__cstring: 0x1353
+  __TEXT.__oslogstring: 0xc6f
+  __TEXT.__objc_methname: 0x1939
   __TEXT.__objc_classname: 0x20b
-  __TEXT.__objc_methtype: 0x8ab
-  __TEXT.__unwind_info: 0x2e8
-  __DATA_CONST.__auth_got: 0x310
-  __DATA_CONST.__got: 0x110
-  __DATA_CONST.__const: 0x580
-  __DATA_CONST.__cfstring: 0x340
+  __TEXT.__objc_methtype: 0x869
+  __TEXT.__unwind_info: 0x2d0
+  __DATA_CONST.__auth_got: 0x318
+  __DATA_CONST.__got: 0x118
+  __DATA_CONST.__const: 0x530
+  __DATA_CONST.__cfstring: 0x360
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x50
-  __DATA.__objc_const: 0x1188
-  __DATA.__objc_selrefs: 0x758
-  __DATA.__objc_ivar: 0x9c
+  __DATA.__objc_const: 0x11a0
+  __DATA.__objc_selrefs: 0x730
+  __DATA.__objc_ivar: 0xa0
   __DATA.__objc_data: 0x320
   __DATA.__data: 0x668
   __DATA.__bss: 0x88
+  - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HomeKit.framework/HomeKit

   - /System/Library/PrivateFrameworks/SiriKitRuntime.framework/SiriKitRuntime
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6CA5CB31-8E80-3304-994C-71D63AEB46E8
-  Functions: 193
-  Symbols:   139
-  CStrings:  631
+  UUID: BF0A0CC1-FEF2-3EED-BC66-511FCADA8B16
+  Functions: 188
+  Symbols:   141
+  CStrings:  616
 
Symbols:
+ _OBJC_CLASS_$_LNDaemonConnectionListener
+ _objc_retain_x28
CStrings:
+ "@\"LNDaemonConnectionListener\""
+ "_lnDaemonConnectionListener"
+ "_loadLNDaemonConnectionListener"
+ "com.apple.assistant_service"
+ "initWithBundleIdentifier:"
- "%s %@ provided verification key %@"
- "%s Class %@ doesn't conform to sync protocol"
- "%s Fetching current sync for path %@"
- "%s Fetching sync info from handler %@"
- "%s No sync class with name %@ at path %@"
- "%s Sync-snapshot timed out, restarting as soon as there are no outstanding commands. Stuck plugin %@ with sync class %@"
- "-[ASServiceClient fetchCurrentSyncSnapshotForServicePath:className:key:completion:]"
- "-[ASServiceClient fetchCurrentSyncSnapshotForServicePath:className:key:completion:]_block_invoke"
- "-[ASServicesMonitor startWatchdogForPluginAtPath:syncClassName:syncSnapshotCompletion:]"
- "-[ASServicesMonitor startWatchdogForPluginAtPath:syncClassName:syncSnapshotCompletion:]_block_invoke"
- "-[ASSyncConnection currentSyncSnapshotFromHandler:forKey:]"
- "Vv48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"AFSyncSnapshot\">40"
- "Vv48@0:8@16@24@32@?40"
- "currentSyncSnapshot"
- "currentSyncSnapshotFromHandler:forKey:"
- "fetchCurrentSyncSnapshotForServicePath:className:key:completion:"
- "forVerification"
- "startWatchdogForPluginAtPath:syncClassName:syncSnapshotCompletion:"
- "syncSnapshotForKey:"
- "syncVerificationKeyForKey:"
- "v16@?0@\"AFSyncSnapshot\"8"

```
