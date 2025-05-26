## UIKit

> `/System/Library/AccessibilityBundles/UIKit.axbundle/UIKit`

```diff

-2909.23.0.0.0
-  __TEXT.__text: 0x16f968
+2909.31.1.0.0
+  __TEXT.__text: 0x16fb94
   __TEXT.__auth_stubs: 0x1450
   __TEXT.__objc_methlist: 0xdf30
   __TEXT.__const: 0x108
   __TEXT.__cstring: 0x17319
-  __TEXT.__oslogstring: 0x2075
+  __TEXT.__oslogstring: 0x2130
   __TEXT.__gcc_except_tab: 0x1e84
   __TEXT.__dlopen_cstrs: 0xb8
   __TEXT.__ustring: 0x78
   __TEXT.__unwind_info: 0x2a74
   __TEXT.__objc_classname: 0x86cc
-  __TEXT.__objc_methname: 0x1511c
+  __TEXT.__objc_methname: 0x15144
   __TEXT.__objc_methtype: 0x21ed
-  __TEXT.__objc_stubs: 0xf9c0
+  __TEXT.__objc_stubs: 0xfa00
   __DATA_CONST.__got: 0x708
   __DATA_CONST.__const: 0x1cf8
   __DATA_CONST.__objc_classlist: 0x1990

   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x114b8
-  __DATA_CONST.__objc_selrefs: 0x53b8
+  __DATA_CONST.__objc_selrefs: 0x53c0
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_classrefs: 0x7e8
   __DATA_CONST.__objc_superrefs: 0x9c8
   __DATA_CONST.__objc_arraydata: 0x170
   __AUTH_CONST.__objc_const: 0xe5e0
   __AUTH_CONST.__cfstring: 0x1bfc0
-  __AUTH_CONST.__const: 0x1380
+  __AUTH_CONST.__const: 0x13a0
   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x48

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5487
-  Symbols:   18726
-  CStrings:  8001
+  Functions: 5492
+  Symbols:   18739
+  CStrings:  8002
 
Symbols:
+ GCC_except_table141
+ GCC_except_table149
+ GCC_except_table164
+ GCC_except_table209
+ GCC_except_table77
+ ___69-[UIApplicationAccessibility _iosAccessibilitySetValue:forAttribute:]_block_invoke.851
+ ___block_literal_global.853
+ ___block_literal_global.888
+ ___block_literal_global.912
+ ___block_literal_global.914
+ ___block_literal_global.929
+ ___block_literal_global.934
+ ___block_literal_global.956
+ ___block_literal_global.965
+ ___block_literal_global.999
+ ___os_log_helper_16_3_2_8_69_8_69
+ ___os_log_helper_16_3_3_8_69_4_0_4_0
+ ___os_log_helper_16_3_3_8_69_8_64_8_64
+ ___os_log_helper_16_3_3_8_69_8_69_8_69
+ __unnamed_array_storage.972
+ __unnamed_array_storage.979
+ __unnamed_array_storage.980
+ __unnamed_array_storage.994
+ __unnamed_array_storage.995
+ _objc_msgSend$_accessibilityActivateTextViewLink:
+ _objc_msgSend$showKeyboardIfNeeded
- GCC_except_table140
- GCC_except_table208
- GCC_except_table74
- ___block_literal_global.885
- ___block_literal_global.891
- ___block_literal_global.906
- ___block_literal_global.911
- ___block_literal_global.926
- ___block_literal_global.931
- ___block_literal_global.953
- ___block_literal_global.962
- ___block_literal_global.996
- __unnamed_array_storage.969
- __unnamed_array_storage.976
- __unnamed_array_storage.977
- __unnamed_array_storage.991
- __unnamed_array_storage.992
CStrings:
+ "AX hit test found %{sensitive}@ at converted point %@ for view: %@"
+ "Can't use this view, so keep going: %{sensitive}@ hidden: %d iselement: %d"
+ "Found the view we were looking for through touch forwarding views %{sensitive}@ -> %{sensitive}@"
+ "Hit test: %{sensitive}@ > %@"
+ "Not using this view because it looks like it's a touch forwarding view: parent view: %{sensitive}@, foundView: %{sensitive}@ (forward to: %{sensitive}@)"
+ "Performed further axHitTest post process to get (result %{sensitive}@)"
+ "Point was not inside self %{sensitive}@"
+ "Returning nil because we didn't hit one of our subviews but the point is inside %{sensitive}@"
+ "Returning our allowed modal view %{sensitive}@"
+ "Returning self or subview of self (self %{sensitive}@, result %{sensitive}@)"
+ "Returning the matching UIA test object: %{sensitive}@"
+ "Returning the view we found via AX hit test %{sensitive}@"
+ "Something blocks the view we found, so skipping it.  We also uncache our first good view for some reason...: %{sensitive}@"
+ "_accessibilityActivateTextViewLink:"
- "AX hit test found %@ at converted point %@ for view: %@"
- "Can't use this view, so keep going: %@ hidden: %d iselement: %d"
- "Found the view we were looking for through touch forwarding views %@ -> %@"
- "Hit test: %@ > %@"
- "Not using this view because it looks like it's a touch forwarding view: parent view: %@, foundView: %@ (forward to: %@)"
- "Performed further axHitTest post process to get (result %@)"
- "Point was not inside self %@"
- "Returning nil because we didn't hit one of our subviews but the point is inside %@"
- "Returning our allowed modal view %@"
- "Returning self or subview of self (self %@, result %@)"
- "Returning the matching UIA test object: %@"
- "Returning the view we found via AX hit test %@"
- "Something blocks the view we found, so skipping it.  We also uncache our first good view for some reason...: %@"

```
