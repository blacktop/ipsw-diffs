## StoreKit

> `/System/Library/Frameworks/StoreKit.framework/StoreKit`

```diff

-815.1.6.0.0
-  __TEXT.__text: 0x174bc8
-  __TEXT.__auth_stubs: 0x3120
-  __TEXT.__objc_methlist: 0x5cc4
+815.1.12.0.0
+  __TEXT.__text: 0x17631c
+  __TEXT.__auth_stubs: 0x3160
+  __TEXT.__objc_methlist: 0x5d24
   __TEXT.__gcc_except_tab: 0x109c
-  __TEXT.__const: 0xfda4
+  __TEXT.__const: 0xfe74
   __TEXT.__oslogstring: 0x35c0
-  __TEXT.__cstring: 0x7f57
+  __TEXT.__cstring: 0x8037
   __TEXT.__dlopen_cstrs: 0x498
-  __TEXT.__constg_swiftt: 0x33e8
-  __TEXT.__swift5_typeref: 0x423c
+  __TEXT.__constg_swiftt: 0x3404
+  __TEXT.__swift5_typeref: 0x424a
   __TEXT.__swift5_builtin: 0x168
-  __TEXT.__swift5_reflstr: 0x2ae4
-  __TEXT.__swift5_fieldmd: 0x3f48
+  __TEXT.__swift5_reflstr: 0x2b14
+  __TEXT.__swift5_fieldmd: 0x3f70
   __TEXT.__swift5_assocty: 0x980
-  __TEXT.__swift5_proto: 0xe34
-  __TEXT.__swift5_types: 0x4f0
+  __TEXT.__swift5_proto: 0xe40
+  __TEXT.__swift5_types: 0x4f4
   __TEXT.__swift5_capture: 0x18bc
   __TEXT.__swift_as_entry: 0x460
   __TEXT.__swift_as_ret: 0x448
   __TEXT.__swift5_mpenum: 0x40
   __TEXT.__swift5_protos: 0x28
-  __TEXT.__unwind_info: 0x6f38
-  __TEXT.__eh_frame: 0xbd18
-  __TEXT.__objc_classname: 0x1382
-  __TEXT.__objc_methname: 0xcc83
+  __TEXT.__unwind_info: 0x6f48
+  __TEXT.__eh_frame: 0xbd40
+  __TEXT.__objc_classname: 0x139a
+  __TEXT.__objc_methname: 0xcdad
   __TEXT.__objc_methtype: 0x2fe3
-  __TEXT.__objc_stubs: 0x7da0
-  __DATA_CONST.__got: 0xba8
+  __TEXT.__objc_stubs: 0x7e60
+  __DATA_CONST.__got: 0xbb0
   __DATA_CONST.__const: 0x1898
   __DATA_CONST.__objc_classlist: 0x3f8
-  __DATA_CONST.__objc_catlist: 0x18
+  __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x340
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3090
+  __DATA_CONST.__objc_selrefs: 0x30d8
   __DATA_CONST.__objc_protorefs: 0x198
   __DATA_CONST.__objc_superrefs: 0x208
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0x18a0
-  __AUTH_CONST.__const: 0xe950
-  __AUTH_CONST.__cfstring: 0x3720
-  __AUTH_CONST.__objc_const: 0x14bb0
+  __AUTH_CONST.__auth_got: 0x18c0
+  __AUTH_CONST.__const: 0xe9e0
+  __AUTH_CONST.__cfstring: 0x3740
+  __AUTH_CONST.__objc_const: 0x14c78
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x2680
-  __AUTH.__data: 0x2448
-  __DATA.__objc_ivar: 0x5a8
-  __DATA.__data: 0x5ca0
-  __DATA.__bss: 0x1ae90
+  __AUTH.__data: 0x2438
+  __DATA.__objc_ivar: 0x5b0
+  __DATA.__data: 0x5cd8
+  __DATA.__bss: 0x1b010
   __DATA.__common: 0x98
   __DATA_DIRTY.__objc_data: 0x370
   __DATA_DIRTY.__data: 0x240

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: AB60CF59-FB65-3C3E-8C6F-A14121D34FEF
-  Functions: 11446
-  Symbols:   15392
-  CStrings:  4411
+  UUID: BD51AE87-5E9E-37CE-A95B-4CCA56CE122F
+  Functions: 11487
+  Symbols:   15481
+  CStrings:  4433
 
Symbols:
+ -[SKMutablePayment setMetricsOverlay:]
+ -[SKPayment metricsOverlay]
+ -[SKStoreReviewViewController initWithReviewRequestToken:scene:]
+ -[SKStoreReviewViewController keyboardWillShow:]
+ -[SKStoreReviewViewController scene]
+ -[UIApplication(KeyboardNotifications) activeFirstResponder]
+ -[UIApplication(KeyboardNotifications) resignFirstResponderInScene:]
+ -[UIApplication(KeyboardNotifications) restoreFirstResponder]
+ -[UIApplication(KeyboardNotifications) setActiveFirstResponder:]
+ _OBJC_IVAR_$_SKPaymentInternal._metricsOverlay
+ _OBJC_IVAR_$_SKStoreReviewViewController._scene
+ _SKPaymentOptionMetricsOverlayData
+ _UIKeyboardWillShowNotification
+ _UIModalTransitionStyleWrapperToUIModalTransitionStyle
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_UIApplication_$_KeyboardNotifications
+ __OBJC_$_CATEGORY_UIApplication_$_KeyboardNotifications
+ __OBJC_$_PROP_LIST_UIApplication_$_KeyboardNotifications
+ ___swift_memcpy25_8
+ _associated conformance 8StoreKit7ProductV14PurchaseOptionV0dE5ErrorOSHAASQ
+ _block_copy_helper.64
+ _block_copy_helper.70
+ _block_descriptor.66
+ _block_descriptor.72
+ _block_destroy_helper.65
+ _block_destroy_helper.71
+ _objc_getAssociatedObject
+ _objc_msgSend$activeFirstResponder
+ _objc_msgSend$becomeFirstResponder
+ _objc_msgSend$endEditing:
+ _objc_msgSend$initWithReviewRequestToken:scene:
+ _objc_msgSend$resignFirstResponderInScene:
+ _objc_msgSend$restoreFirstResponder
+ _objc_msgSend$setActiveFirstResponder:
+ _objc_setAssociatedObject
+ _symbolic _____ 8StoreKit7ProductV14PurchaseOptionV0dE5ErrorO
- -[SKStoreReviewViewController initWithReviewRequestToken:]
- GCC_except_table6
- _block_copy_helper.59
- _block_copy_helper.65
- _block_descriptor.61
- _block_descriptor.67
- _block_destroy_helper.60
- _block_destroy_helper.66
- _objc_msgSend$initWithReviewRequestToken:
CStrings:
+ "\"metricsOverlay\""
+ ") for last app store action."
+ "23:41:22"
+ "Failed to serialize metrics overlay: "
+ "Invalid adamID ("
+ "KeyboardNotifications"
+ "Metrics overlay is not a valid JSON object"
+ "Sep 28 2025"
+ "T@\"NSDictionary\",&,D,N"
+ "T@\"NSDictionary\",R,N"
+ "T@\"UIResponder\",&,N"
+ "T@\"UIWindowScene\",R,N,V_scene"
+ "_metricsOverlay"
+ "activeFirstResponder"
+ "becomeFirstResponder"
+ "endEditing:"
+ "initWithReviewRequestToken:scene:"
+ "keyboardWillShow:"
+ "metrics-overlay-data"
+ "metricsOverlay"
+ "resignFirstResponderInScene:"
+ "restoreFirstResponder"
+ "setActiveFirstResponder:"
+ "setMetricsOverlay:"
- "00:22:25"
- "Sep 17 2025"
- "initWithReviewRequestToken:"

```
