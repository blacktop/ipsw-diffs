## AuthenticationServicesCore

> `/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/AuthenticationServicesCore`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-625.1.22.10.3
-  __TEXT.__text: 0xc8508
-  __TEXT.__objc_methlist: 0x3b4c
+625.1.24.10.1
+  __TEXT.__text: 0xc8a6c
+  __TEXT.__objc_methlist: 0x3b7c
   __TEXT.__const: 0xcd08
-  __TEXT.__cstring: 0x3cd1
-  __TEXT.__oslogstring: 0x40c0
+  __TEXT.__cstring: 0x3d11
+  __TEXT.__oslogstring: 0x4150
   __TEXT.__gcc_except_tab: 0x334
   __TEXT.__ustring: 0x564
   __TEXT.__dlopen_cstrs: 0x48

   __TEXT.__swift_as_cont: 0xe4
   __TEXT.__swift5_protos: 0x28
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x3538
+  __TEXT.__unwind_info: 0x3548
   __TEXT.__eh_frame: 0x4688
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__const: 0xcd0
   __DATA_CONST.__objc_classlist: 0x208
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x180
+  __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ea8
+  __DATA_CONST.__objc_selrefs: 0x1ec0
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x10
-  __DATA_CONST.__got: 0x8d8
+  __DATA_CONST.__got: 0x8e0
   __AUTH_CONST.__const: 0x6588
-  __AUTH_CONST.__cfstring: 0x2060
-  __AUTH_CONST.__objc_const: 0x7ea0
+  __AUTH_CONST.__cfstring: 0x20c0
+  __AUTH_CONST.__objc_const: 0x7ec0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x13f8
+  __AUTH_CONST.__auth_got: 0x1400
   __AUTH.__objc_data: 0x480
   __AUTH.__data: 0x828
   __DATA.__objc_ivar: 0x438
-  __DATA.__data: 0x25a0
+  __DATA.__data: 0x2600
   __DATA.__bss: 0x10fd0
   __DATA.__common: 0x148
   __DATA_DIRTY.__objc_data: 0x2590

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4997
-  Symbols:   4092
-  CStrings:  786
+  Functions: 5002
+  Symbols:   4106
+  CStrings:  791
 
Symbols:
+ -[ASCAgent _credentialRequestedForCABLELoginChoice:completionHandler:]
+ -[ASCAgent getSafariPasswordAutoFillSettingWithCompletionHandler:]
+ -[ASCAgentProxy getSafariPasswordAutoFillSettingWithCompletionHandler:]
+ GCC_except_table131
+ GCC_except_table175
+ GCC_except_table178
+ GCC_except_table61
+ GCC_except_table76
+ _WBSOSLogAutoFill
+ _WBSWebExtensionPointIdentifier
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ASCSafariSettingsHelperProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ASCSafariSettingsHelperProtocol
+ __OBJC_$_PROTOCOL_REFS_ASCSafariSettingsHelperProtocol
+ __OBJC_LABEL_PROTOCOL_$_ASCSafariSettingsHelperProtocol
+ __OBJC_PROTOCOL_$_ASCSafariSettingsHelperProtocol
+ ___70-[ASCAgent _credentialRequestedForCABLELoginChoice:completionHandler:]_block_invoke
+ ___70-[ASCAgent _credentialRequestedForCABLELoginChoice:completionHandler:]_block_invoke_2
+ ___71-[ASCAgentProxy getSafariPasswordAutoFillSettingWithCompletionHandler:]_block_invoke
+ ___71-[ASCAgentProxy getSafariPasswordAutoFillSettingWithCompletionHandler:]_block_invoke_2
+ _objc_msgSend$_credentialRequestedForCABLELoginChoice:completionHandler:
+ _objc_msgSend$getSafariPasswordAutoFillSettingWithCompletionHandler:
+ _objc_msgSend$infoDictionary
+ _objc_msgSend$safari_boolForKey:defaultValue:
- -[ASCAgent _credentialRequestedForCABLELoginChoice:]
- GCC_except_table130
- GCC_except_table174
- GCC_except_table177
- GCC_except_table60
- GCC_except_table72
- ___52-[ASCAgent _credentialRequestedForCABLELoginChoice:]_block_invoke
- ___52-[ASCAgent _credentialRequestedForCABLELoginChoice:]_block_invoke_2
- _objc_msgSend$_credentialRequestedForCABLELoginChoice:
CStrings:
+ "AutoFillPasswordsInSafari"
+ "Client process is not allowed to read Safari AutoFill settings"
+ "Failed to get extension record for application identifier with error: %{public}@"
+ "NSExtension"
+ "NSExtensionPointIdentifier"
```
