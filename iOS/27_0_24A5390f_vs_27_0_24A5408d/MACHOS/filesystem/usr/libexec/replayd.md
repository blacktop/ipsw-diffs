## replayd

> `/usr/libexec/replayd`

### Sections with Same Size but Changed Content

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
-  __TEXT.__text: 0xb7fa0
+740.63.1.1.0
+  __TEXT.__text: 0xb8c4c
   __TEXT.__auth_stubs: 0x1910
-  __TEXT.__objc_stubs: 0xf000
-  __TEXT.__objc_methlist: 0x7378
+  __TEXT.__objc_stubs: 0xf060
+  __TEXT.__objc_methlist: 0x73c8
   __TEXT.__const: 0x3e4
-  __TEXT.__gcc_except_tab: 0xfa4
-  __TEXT.__objc_methname: 0x15c42
-  __TEXT.__oslogstring: 0x15f42
-  __TEXT.__cstring: 0x1787a
+  __TEXT.__gcc_except_tab: 0xfbc
+  __TEXT.__objc_methname: 0x15d0c
+  __TEXT.__oslogstring: 0x1626c
+  __TEXT.__cstring: 0x17a78
   __TEXT.__objc_classname: 0xa44
-  __TEXT.__objc_methtype: 0x43c3
-  __TEXT.__unwind_info: 0x22c0
-  __DATA_CONST.__const: 0x2a70
-  __DATA_CONST.__cfstring: 0x5ca0
+  __TEXT.__objc_methtype: 0x4403
+  __TEXT.__unwind_info: 0x22f8
+  __DATA_CONST.__const: 0x2a98
+  __DATA_CONST.__cfstring: 0x5cc0
   __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x130

   __DATA_CONST.__auth_got: 0xc98
   __DATA_CONST.__got: 0xc88
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x11278
-  __DATA.__objc_selrefs: 0x4670
-  __DATA.__objc_ivar: 0xd6c
+  __DATA.__objc_const: 0x11310
+  __DATA.__objc_selrefs: 0x4690
+  __DATA.__objc_ivar: 0xd7c
   __DATA.__objc_data: 0x18b0
   __DATA.__data: 0xe54
   __DATA.__bss: 0x258

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3622
+  Functions: 3634
   Symbols:   801
-  CStrings:  7310
+  CStrings:  7335
 
CStrings:
+ " [ERROR] %{public}s:%d Picker cancelled but pickerConfig is nil - cannot notify app"
+ " [ERROR] %{public}s:%d pickerDidEnd rejected: caller lacks ScreenCaptureKit private entitlement"
+ " [ERROR] %{public}s:%d pickerDidUpdate rejected: caller lacks ScreenCaptureKit private entitlement"
+ " [ERROR] %{public}s:%d startCapture rejected: filterID=%@ was not vended by the picker for app=%@"
+ " [ERROR] %{public}s:%d startCapture rejected: full-display filterID=%@ consumed or expired for app=%@"
+ " [ERROR] %{public}s:%d validateFilterForStart: missing filterID"
+ " [INFO] %{public}s:%d Control Center host disconnected, clearing presented ScreenCaptureKit picker info"
+ " [INFO] %{public}s:%d Picker cancelled - notifying app"
+ " [INFO] %{public}s:%d Picker state cleared"
+ " [INFO] %{public}s:%d pickerDidDismiss isCancelled=%d stream=%@"
+ " [INFO] %{public}s:%d timerDidUpdate: stale timer tick after recording output removed; skipping"
+ "-[RPClient validateFilterForStart:]"
+ "-[RPConnectionManager pickerDidDismiss:forStream:isCancelled:]_block_invoke"
+ "-[RPConnectionManager pickerDidEnd:withFilter:forStream:]"
+ "-[RPConnectionManager pickerDidUpdate:withFilter:preservedFilter:forStream:completionHandler:]"
+ "-[RPRecordingManager pickerDidDismiss:forStream:isCancelled:]"
+ "The content filter cannot be used to start a stream. A full-display filter obtained from the system picker is single-use and must be re-presented via the picker for each new stream."
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
+ "validateFilterForStart:"
- " [INFO] %{public}s:%d skip notify control center manager for stream with only recording output"
- "T@\"SCPrivacyAlert\",R,N,V_privacyAlert"
- "privacyAlert"
```
