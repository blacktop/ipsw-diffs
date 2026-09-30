## appconduitd

> `/System/Library/PrivateFrameworks/AppConduit.framework/Support/appconduitd`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-405.0.0.0.0
-  __TEXT.__text: 0x59a34
+408.0.0.0.0
+  __TEXT.__text: 0x59b6c
   __TEXT.__auth_stubs: 0x9f0
-  __TEXT.__objc_stubs: 0x7fc0
-  __TEXT.__objc_methlist: 0x3c74
-  __TEXT.__const: 0xc8
+  __TEXT.__objc_stubs: 0x8060
+  __TEXT.__objc_methlist: 0x3c8c
+  __TEXT.__const: 0xd0
   __TEXT.__gcc_except_tab: 0xb24
-  __TEXT.__objc_methname: 0xbe9a
-  __TEXT.__cstring: 0x14e7e
+  __TEXT.__objc_methname: 0xbf49
+  __TEXT.__cstring: 0x14efd
   __TEXT.__objc_classname: 0x594
   __TEXT.__objc_methtype: 0x1e52
-  __TEXT.__oslogstring: 0x1a0
-  __TEXT.__unwind_info: 0x12a0
-  __DATA_CONST.__const: 0x18f8
-  __DATA_CONST.__cfstring: 0x9380
+  __TEXT.__oslogstring: 0x1ea
+  __TEXT.__unwind_info: 0x1290
+  __DATA_CONST.__const: 0x1900
+  __DATA_CONST.__cfstring: 0x93c0
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xa0

   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_arrayobj: 0x90
   __DATA_CONST.__auth_got: 0x508
-  __DATA_CONST.__got: 0x410
+  __DATA_CONST.__got: 0x418
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x8ae8
-  __DATA.__objc_selrefs: 0x25e8
+  __DATA.__objc_const: 0x8b08
+  __DATA.__objc_selrefs: 0x2610
   __DATA.__objc_ivar: 0x3f0
   __DATA.__objc_data: 0xbe0
   __DATA.__data: 0x7c0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1599
-  Symbols:   302
-  CStrings:  3653
+  Functions: 1602
+  Symbols:   303
+  CStrings:  3661
 
Symbols:
+ _OBJC_CLASS_$_ACXFeatureFlags
CStrings:
+ "ACX_isDeletable"
+ "ACX_isDeletableSystemApp"
+ "Failed to post restricted distributed notification %{public}@: %{public}@"
+ "Jul 10 2026"
+ "Posting restricted distributed notification %@ with payload %@"
+ "Posting unrestricted distributed notification %@ with payload %@"
+ "bundleContainerURL"
+ "com.apple.appconduit.remote-app-notifications.read"
+ "postNotificationName:object:userInfo:audience:entitlement:options:error:"
+ "restrictedDistributedNotificationsEnabled"
- "Jun 26 2026"
- "Posting distributed notification %@ with payload %@"
```
