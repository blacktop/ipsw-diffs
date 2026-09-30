## StackshotDelegateComponent

> `/System/ExclaveKit/System/Library/Frameworks/StackshotDelegateComponent.framework/StackshotDelegateComponent`

```diff

 26.60.20.0.0
-  __TEXT.__text: 0x4b34
+  __TEXT.__text: 0x4ba8
   __TEXT.__auth_stubs: 0x260
   __TEXT.__const: 0x70
-  __TEXT.__cstring: 0xfdc
-  __TEXT.__unwind_info: 0x170
+  __TEXT.__cstring: 0xf73
+  __TEXT.__unwind_info: 0x178
   __DATA.__auth_got: 0x130
   __DATA.__got: 0x10
   __DATA.__auth_ptr: 0x8
-  __DATA.__const: 0x5e0
+  __DATA.__const: 0x5f0
   __DATA.__data: 0xe0
   __DATA.__TIGHTBEAM: 0x10
   __DATA.__bss: 0x8
Symbols:
+ __asid__v_encode_block_invoke.95
+ __block_descriptor_tmp.31
+ __block_descriptor_tmp.34
+ __block_descriptor_tmp.39
+ __block_descriptor_tmp.43
+ __block_descriptor_tmp.46
+ __block_descriptor_tmp.49
+ __block_descriptor_tmp.62
+ __block_descriptor_tmp.73
+ __block_descriptor_tmp.80
+ __block_descriptor_tmp.87
+ __block_descriptor_tmp.91
+ __block_descriptor_tmp.94
+ __decodeStackshotDelegateComponent2_block_invoke.69
+ __decodeStackshotDelegateComponent2_block_invoke.69.cold.1
+ __decodeStackshotDelegateComponent2_block_invoke.76
+ __decodeStackshotDelegateComponent2_block_invoke.76.cold.1
+ __decodeStackshotDelegateComponent2_block_invoke.83
+ __stackshottypes_textsegment__v_encode_block_invoke.35
+ __u8__v_encode_block_invoke.47
- __asid__v_encode_block_invoke.97
- __block_descriptor_tmp.29
- __block_descriptor_tmp.35
- __block_descriptor_tmp.40
- __block_descriptor_tmp.41
- __block_descriptor_tmp.45
- __block_descriptor_tmp.50
- __block_descriptor_tmp.51
- __block_descriptor_tmp.64
- __block_descriptor_tmp.75
- __block_descriptor_tmp.82
- __block_descriptor_tmp.89
- __block_descriptor_tmp.93
- __block_descriptor_tmp.98
- __decodeStackshotDelegateComponent2_block_invoke.71
- __decodeStackshotDelegateComponent2_block_invoke.71.cold.1
- __decodeStackshotDelegateComponent2_block_invoke.78
- __decodeStackshotDelegateComponent2_block_invoke.78.cold.1
- __decodeStackshotDelegateComponent2_block_invoke.85
- __stackshottypes_textsegment__v_encode_block_invoke.39
- __u8__v_encode_block_invoke.49
CStrings:
+ "TB_FATAL: invalid error returned from getAddressSpaceInfo (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from getIPCStackEntry (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid value: unexpected case value, %!l(MISSING)lx (%!s(MISSING):%!d(MISSING))\n"
- "(address__v_decode(message, &opt->value) == TB_ERROR_SUCCESS) && \"failed to decode type: StackshotTypes.Address (aka. UInt64)\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from getAddressSpaceInfo\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from getIPCStackEntry\""

```
