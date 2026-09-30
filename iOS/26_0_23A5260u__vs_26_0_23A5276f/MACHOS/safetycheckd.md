## safetycheckd

> `/usr/libexec/safetycheckd`

```diff

-552.0.0.0.0
-  __TEXT.__text: 0x2900
+565.0.1.0.0
+  __TEXT.__text: 0x2550
   __TEXT.__auth_stubs: 0x2e0
   __TEXT.__objc_stubs: 0xa40
   __TEXT.__objc_methlist: 0x4c8
-  __TEXT.__const: 0x38
-  __TEXT.__objc_methname: 0xac0
-  __TEXT.__oslogstring: 0x225
-  __TEXT.__objc_classname: 0xe8
-  __TEXT.__objc_methtype: 0x34d
-  __TEXT.__cstring: 0x215
+  __TEXT.__const: 0x28
+  __TEXT.__objc_methname: 0xa2f
+  __TEXT.__oslogstring: 0x129
+  __TEXT.__objc_classname: 0xea
+  __TEXT.__objc_methtype: 0x335
+  __TEXT.__cstring: 0x1db
   __TEXT.__gcc_except_tab: 0x10
-  __TEXT.__unwind_info: 0x140
+  __TEXT.__unwind_info: 0x138
   __DATA_CONST.__auth_got: 0x180
   __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0x198
+  __DATA_CONST.__const: 0x120
   __DATA_CONST.__cfstring: 0x180
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA.__objc_const: 0x8a0
-  __DATA.__objc_selrefs: 0x368
-  __DATA.__objc_ivar: 0x38
+  __DATA.__objc_const: 0x860
+  __DATA.__objc_selrefs: 0x360
+  __DATA.__objc_ivar: 0x30
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x248
   __DATA.__bss: 0x30

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AFDF9C40-08AC-3E7B-9595-BDE088C29B9A
-  Functions: 79
+  UUID: BCD6BF7B-209C-3281-83A9-A68B9E54480C
+  Functions: 76
   Symbols:   76
-  CStrings:  237
+  CStrings:  228
 
Symbols:
+ _OBJC_CLASS_$_DSSourceRepository
+ _objc_release_x25
+ _objc_retain_x4
- _OBJC_CLASS_$_DSError
- _dispatch_async
- _objc_retain_x22
CStrings:
+ "containsObject:"
+ "sourceNames"
+ "sources"
+ "sourcesWithNames:"
+ "stopSharingSources:queue:completion:"
- "\"Trying to stop all sharing for person %{private}@, but they aren't in the permissions model\""
- "\"Trying to stop selected sharing for person %{private}@, but they aren't in the permissions model\""
- "@\"DSSharingPermissions\""
- "@\"Stopping sharing from %{public}@ for person %{private}@\""
- "T@\"DSSharingPermissions\",&,N,V_permissions"
- "_dispatchQueue"
- "_permissions"
- "com.apple.safetycheckd.SCPermissionsService.dispatchQueue"
- "matchesXPCRepresentation:"
- "permissions"
- "personInModelMatchingShallowPerson:"
- "setPermissions:"
- "stopAllSharingOnQueue:completion:"
- "stopSharingSourceNames:queue:completion:"

```
