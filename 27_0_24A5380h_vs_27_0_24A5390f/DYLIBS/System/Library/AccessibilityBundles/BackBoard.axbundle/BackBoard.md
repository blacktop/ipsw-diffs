## BackBoard

> `/System/Library/AccessibilityBundles/BackBoard.axbundle/BackBoard`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-3042.0.0.0.0
-  __TEXT.__text: 0x27d9c
+3045.0.0.0.0
+  __TEXT.__text: 0x27e4c
   __TEXT.__objc_methlist: 0x22d4
   __TEXT.__dlopen_cstrs: 0x2d9
   __TEXT.__const: 0x500
   __TEXT.__cstring: 0x2317
-  __TEXT.__oslogstring: 0x1e8a
+  __TEXT.__oslogstring: 0x1e62
   __TEXT.__constg_swiftt: 0x2e0
   __TEXT.__swift5_typeref: 0x17e
   __TEXT.__swift5_reflstr: 0x115

   __TEXT.__swift_as_ret: 0x14
   __TEXT.__swift_as_cont: 0x18
   __TEXT.__gcc_except_tab: 0x698
-  __TEXT.__unwind_info: 0xd10
+  __TEXT.__unwind_info: 0xd08
   __TEXT.__eh_frame: 0x218
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1bc8
+  __DATA_CONST.__objc_selrefs: 0x1bd8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_arraydata: 0x80
-  __DATA_CONST.__got: 0x6a0
+  __DATA_CONST.__got: 0x6a8
   __AUTH_CONST.__const: 0xfa0
   __AUTH_CONST.__cfstring: 0x1d60
   __AUTH_CONST.__objc_const: 0x3038

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1018
-  Symbols:   2824
-  CStrings:  487
+  Functions: 1017
+  Symbols:   2826
+  CStrings:  486
 
Symbols:
+ -[AXBAccessibilityManager _sendPressFingerEvent:location:force:flags:contextId:secureName:displayId:fingerIndex:]
+ -[AXBAccessibilityManager simulatePressAtPoint:withContextId:withDelay:withForce:withSecureName:displayId:fingerIndex:]
+ GCC_except_table520
+ GCC_except_table566
+ GCC_except_table595
+ GCC_except_table612
+ GCC_except_table625
+ GCC_except_table637
+ GCC_except_table670
+ GCC_except_table708
+ GCC_except_table722
+ GCC_except_table796
+ _kAXSimulatePressAtPointActionKeyDisplayID
+ _objc_msgSend$_sendPressFingerEvent:location:force:flags:contextId:secureName:displayId:fingerIndex:
+ _objc_msgSend$runScrollActionDomainMigrationIfNeeded
+ _objc_msgSend$setDisplayId:
+ _objc_msgSend$simulatePressAtPoint:withContextId:withDelay:withForce:withSecureName:displayId:fingerIndex:
- -[AXBAccessibilityManager _sendPressFingerEvent:location:force:flags:contextId:secureName:fingerIndex:]
- -[AXBAccessibilityManager simulatePressAtPoint:withContextId:withDelay:withForce:withSecureName:fingerIndex:]
- GCC_except_table521
- GCC_except_table567
- GCC_except_table596
- GCC_except_table613
- GCC_except_table626
- GCC_except_table638
- GCC_except_table671
- GCC_except_table709
- GCC_except_table723
- GCC_except_table797
- __deviceInStateRequiringVoiceOverTripleClickInBuddy
- _objc_msgSend$_sendPressFingerEvent:location:force:flags:contextId:secureName:fingerIndex:
- _objc_msgSend$simulatePressAtPoint:withContextId:withDelay:withForce:withSecureName:fingerIndex:
CStrings:
- "Buddy running: %d, LoginUI: %d, IOD: %d"
```
