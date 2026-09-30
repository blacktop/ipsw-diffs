## replayd

> `/usr/libexec/replayd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-740.57.1.0.0
-  __TEXT.__text: 0xc6700
+740.62.1.0.0
+  __TEXT.__text: 0xc6c68
   __TEXT.__auth_stubs: 0x1b10
-  __TEXT.__objc_stubs: 0xeca0
-  __TEXT.__objc_methlist: 0x7574
+  __TEXT.__objc_stubs: 0xed00
+  __TEXT.__objc_methlist: 0x75ac
   __TEXT.__const: 0x430
-  __TEXT.__oslogstring: 0x15411
-  __TEXT.__cstring: 0x17289
+  __TEXT.__oslogstring: 0x15545
+  __TEXT.__cstring: 0x17314
   __TEXT.__objc_classname: 0xacb
-  __TEXT.__objc_methname: 0x160db
-  __TEXT.__objc_methtype: 0x409d
-  __TEXT.__gcc_except_tab: 0xfcc
+  __TEXT.__objc_methname: 0x1618d
+  __TEXT.__objc_methtype: 0x40dd
+  __TEXT.__gcc_except_tab: 0xfe4
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__unwind_info: 0x22f8
-  __DATA_CONST.__const: 0x28d0
+  __TEXT.__unwind_info: 0x2320
+  __DATA_CONST.__const: 0x2900
   __DATA_CONST.__cfstring: 0x6360
   __DATA_CONST.__objc_classlist: 0x2e0
   __DATA_CONST.__objc_catlist: 0x30

   __DATA_CONST.__auth_got: 0xd98
   __DATA_CONST.__got: 0xd08
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA.__objc_const: 0x110e8
-  __DATA.__objc_selrefs: 0x4650
-  __DATA.__objc_ivar: 0xdd8
+  __DATA.__objc_const: 0x11180
+  __DATA.__objc_selrefs: 0x4668
+  __DATA.__objc_ivar: 0xde8
   __DATA.__objc_data: 0x1cc0
   __DATA.__data: 0xc98
   __DATA.__bss: 0x290

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3745
+  Functions: 3752
   Symbols:   848
-  CStrings:  7396
+  CStrings:  7409
 
CStrings:
+ " [ERROR] %{public}s:%d pickerDidDismiss is not supported on macOS and should not be called"
+ " [ERROR] %{public}s:%d session=%p screenshot frame complete but has no image buffer, failing request streamID=%{public}@"
+ " [INFO] %{public}s:%d timerDidUpdate: stale timer tick after recording output removed; skipping"
+ "-[RPConnectionManager pickerDidDismiss:forStream:isCancelled:]_block_invoke"
+ "-[RPRecordingManager pickerDidDismiss:forStream:isCancelled:]"
+ "Vv36@0:8@\"NSDictionary\"16@\"NSDictionary\"24B32"
+ "Vv36@0:8@16@24B32"
+ "_privacyAlertLock"
+ "_vendedFilterID"
+ "_vendedFilterLock"
+ "_vendedFilterVendTime"
+ "createPrivacyAlertIfNeeded"
+ "pickerDidDismiss:forStream:isCancelled:"
+ "presentPrivacyAlertWithOptions:completionHandler:"
+ "shouldPresentPrivacyAlertWithOptions:"
- "T@\"SCPrivacyAlert\",R,N,V_privacyAlert"
- "privacyAlert"
```
