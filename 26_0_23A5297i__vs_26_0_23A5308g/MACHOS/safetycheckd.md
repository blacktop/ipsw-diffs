## safetycheckd

> `/usr/libexec/safetycheckd`

```diff

-574.0.0.0.0
-  __TEXT.__text: 0x8920
-  __TEXT.__auth_stubs: 0x4d0
-  __TEXT.__objc_stubs: 0xf20
-  __TEXT.__objc_methlist: 0x508
+579.0.0.0.0
+  __TEXT.__text: 0x8d0c
+  __TEXT.__auth_stubs: 0x4f0
+  __TEXT.__objc_stubs: 0xec0
+  __TEXT.__objc_methlist: 0x4f0
   __TEXT.__const: 0x50
-  __TEXT.__objc_methname: 0xe90
-  __TEXT.__oslogstring: 0x8f6
+  __TEXT.__objc_methname: 0xe59
+  __TEXT.__oslogstring: 0xa37
   __TEXT.__objc_classname: 0xeb
   __TEXT.__objc_methtype: 0x373
-  __TEXT.__cstring: 0x326
-  __TEXT.__gcc_except_tab: 0x644
-  __TEXT.__unwind_info: 0x1c0
-  __DATA_CONST.__auth_got: 0x278
+  __TEXT.__cstring: 0x36c
+  __TEXT.__gcc_except_tab: 0x608
+  __TEXT.__unwind_info: 0x1f8
+  __DATA_CONST.__auth_got: 0x288
   __DATA_CONST.__got: 0x168
-  __DATA_CONST.__const: 0x2b0
-  __DATA_CONST.__cfstring: 0x200
+  __DATA_CONST.__const: 0x378
+  __DATA_CONST.__cfstring: 0x220
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA.__objc_const: 0x8c0
-  __DATA.__objc_selrefs: 0x498
-  __DATA.__objc_ivar: 0x44
+  __DATA.__objc_const: 0x880
+  __DATA.__objc_selrefs: 0x480
+  __DATA.__objc_ivar: 0x40
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x248
   __DATA.__bss: 0x38

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CD3C2031-EA90-3E0D-9B2C-5F2DAA939720
-  Functions: 106
-  Symbols:   131
-  CStrings:  354
+  UUID: D104654C-667C-3476-924C-6DBB24E0C67A
+  Functions: 111
+  Symbols:   133
+  CStrings:  356
 
Symbols:
+ _dispatch_group_wait
+ _dispatch_time
CStrings:
+ "@\"NSObject<OS_dispatch_queue_attr>\""
+ "Failed to fetch shared resources due to timeout"
+ "Finished working with %@"
+ "Found DSParticipation %@ matching UI representation %@"
+ "Found participant matching %@ at idx %ld, but the retrieved participant is null"
+ "None"
+ "_priorityAttribute"
+ "_stopSharingEachParticipant:fromSource:completion:"
+ "_stopSharingParticipants: %{private}@ from source %{public}@"
+ "_stopSharingParticipants:fromSource:completion:"
+ "com.apple.safetycheckd.SCPermissionsService.stopSharingWorkQueue"
+ "stopSharingParticipation:fromSource:completion:"
+ "stopSharingWithParticipants: Fetching sharing from %@"
+ "stopSharingWithParticipants: Finished fetching sharing from %@. Error: %@"
+ "stopSharingWithSource: %@ participants: %@"
- "@\"DSSourceRepository\""
- "Stopping sharing of participants %{private}@ from source %{public}@"
- "T@\"DSSourceRepository\",&,N,V_repo"
- "T@\"NSMutableDictionary\",&,N,V_participantsBySource"
- "_participantsBySource"
- "_repo"
- "fetchedParticipants:forSource:"
- "participantsBySource"
- "removeAllObjects"
- "repo"
- "setParticipantsBySource:"
- "setRepo:"
- "stopSharingWithSource: %@ originalParticipants: %@"
- "v32@0:8@16@24"

```
