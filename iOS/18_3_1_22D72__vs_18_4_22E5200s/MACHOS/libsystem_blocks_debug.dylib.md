## libsystem_blocks_debug.dylib

> `/System/ExclaveKit/usr/lib/system/libsystem_blocks_debug.dylib`

```diff

-95.0.0.0.0
-  __TEXT.__text: 0x2108
+96.0.0.0.0
+  __TEXT.__text: 0x1f58
   __TEXT.__auth_stubs: 0x90
   __TEXT.__objc_methlist: 0x118
   __TEXT.__const: 0x70
+  __TEXT.__cstring: 0x20a
+  __TEXT.__unwind_info: 0xe0
   __TEXT.__objc_classname: 0x6f
   __TEXT.__objc_methname: 0x9d
   __TEXT.__objc_methtype: 0x5d
-  __TEXT.__cstring: 0x20a
-  __TEXT.__unwind_info: 0x148
-  __DATA.__auth_got: 0x48
-  __DATA.__objc_classlist: 0x30
-  __DATA.__objc_nlclslist: 0x30
-  __DATA.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x428
-  __DATA.__objc_selrefs: 0x48
+  __DATA_CONST.__objc_classlist: 0x30
+  __DATA_CONST.__objc_nlclslist: 0x30
+  __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_selrefs: 0x48
+  __AUTH_CONST.__auth_got: 0x48
+  __AUTH_CONST.__objc_const: 0x428
+  __AUTH.__objc_data: 0x1e0
+  __AUTH.__data: 0x18
   __DATA.__objc_ivar: 0x18
-  __DATA.__objc_data: 0x1e0
-  __DATA.__data: 0x18
   - /System/ExclaveKit/usr/lib/libobjc.A.dylib
   - /System/ExclaveKit/usr/lib/system/liblibc.dylib
   - /System/ExclaveKit/usr/lib/system/libsystem_malloc.dylib
   - /System/ExclaveKit/usr/lib/system/libunwind.dylib
-  Functions: 89
-  Symbols:   153
+  Functions: 74
+  Symbols:   175
   CStrings:  48
 
Symbols:
+ _ZN10HelperBaseI13GenericInlineE11copyCaptureILNS1_16BlockCaptureKindE3EEEvj.cold.1
+ _ZN10HelperBaseI13GenericInlineE11copyCaptureILNS1_16BlockCaptureKindE4EEEvj.cold.1
+ _ZN10HelperBaseI13GenericInlineE11copyCaptureILNS1_16BlockCaptureKindE5EEEvj.cold.1
+ _ZN10HelperBaseI13GenericInlineE11copyCaptureILNS1_16BlockCaptureKindE6EEEvj.cold.1
+ _ZN10HelperBaseI13GenericInlineE12destroyBlockEP12Block_layoutbPh.cold.1
+ _ZN10HelperBaseI14ExtendedInlineE11copyCaptureILNS1_16BlockCaptureKindE3EEEvj.cold.1
+ _ZN10HelperBaseI14ExtendedInlineE11copyCaptureILNS1_16BlockCaptureKindE4EEEvj.cold.1
+ _ZN10HelperBaseI14ExtendedInlineE11copyCaptureILNS1_16BlockCaptureKindE5EEEvj.cold.1
+ _ZN10HelperBaseI14ExtendedInlineE11copyCaptureILNS1_16BlockCaptureKindE6EEEvj.cold.1
+ _ZN10HelperBaseI14ExtendedInlineE12destroyBlockEP12Block_layoutbPh.cold.1
+ _ZN10HelperBaseI16GenericOutOfLineE11copyCaptureILNS1_16BlockCaptureKindE3EEEvj.cold.1
+ _ZN10HelperBaseI16GenericOutOfLineE11copyCaptureILNS1_16BlockCaptureKindE4EEEvj.cold.1
+ _ZN10HelperBaseI16GenericOutOfLineE11copyCaptureILNS1_16BlockCaptureKindE5EEEvj.cold.1
+ _ZN10HelperBaseI16GenericOutOfLineE11copyCaptureILNS1_16BlockCaptureKindE6EEEvj.cold.1
+ _ZN10HelperBaseI16GenericOutOfLineE12destroyBlockEP12Block_layoutbPh.cold.1
+ _ZN10HelperBaseI17ExtendedOutOfLineE11copyCaptureILNS1_16BlockCaptureKindE3EEEvj.cold.1
+ _ZN10HelperBaseI17ExtendedOutOfLineE11copyCaptureILNS1_16BlockCaptureKindE4EEEvj.cold.1
+ _ZN10HelperBaseI17ExtendedOutOfLineE11copyCaptureILNS1_16BlockCaptureKindE5EEEvj.cold.1
+ _ZN10HelperBaseI17ExtendedOutOfLineE11copyCaptureILNS1_16BlockCaptureKindE6EEEvj.cold.1
+ _ZN10HelperBaseI17ExtendedOutOfLineE12destroyBlockEP12Block_layoutbPh.cold.1
+ _call_generic_copy_helper.cold.1
+ _call_generic_destroy_helper.cold.1

```
