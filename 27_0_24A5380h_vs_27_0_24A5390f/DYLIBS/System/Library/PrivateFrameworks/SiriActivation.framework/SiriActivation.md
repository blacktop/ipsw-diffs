## SiriActivation

> `/System/Library/PrivateFrameworks/SiriActivation.framework/SiriActivation`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-3600.55.26.0.0
-  __TEXT.__text: 0x6f024
-  __TEXT.__objc_methlist: 0x6ec4
+3600.55.30.0.0
+  __TEXT.__text: 0x6f570
+  __TEXT.__objc_methlist: 0x6f54
   __TEXT.__const: 0x11ac
-  __TEXT.__cstring: 0xca12
-  __TEXT.__oslogstring: 0x90a8
+  __TEXT.__cstring: 0xca82
+  __TEXT.__oslogstring: 0x90da
   __TEXT.__gcc_except_tab: 0xc88
   __TEXT.__dlopen_cstrs: 0x1bc
   __TEXT.__swift5_typeref: 0x732

   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x14
   __TEXT.__swift_as_cont: 0x8c
-  __TEXT.__unwind_info: 0x1e40
+  __TEXT.__unwind_info: 0x1e60
   __TEXT.__eh_frame: 0xee8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1800
-  __DATA_CONST.__objc_classlist: 0x388
+  __DATA_CONST.__const: 0x1808
+  __DATA_CONST.__objc_classlist: 0x390
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x1d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x34d8
+  __DATA_CONST.__objc_selrefs: 0x34f0
   __DATA_CONST.__objc_protorefs: 0x68
-  __DATA_CONST.__objc_superrefs: 0x2c0
+  __DATA_CONST.__objc_superrefs: 0x2c8
   __DATA_CONST.__objc_arraydata: 0x510
-  __DATA_CONST.__got: 0xa58
+  __DATA_CONST.__got: 0xa60
   __AUTH_CONST.__const: 0x1488
-  __AUTH_CONST.__cfstring: 0x4fe0
-  __AUTH_CONST.__objc_const: 0xb068
+  __AUTH_CONST.__cfstring: 0x5000
+  __AUTH_CONST.__objc_const: 0xb138
   __AUTH_CONST.__objc_intobj: 0x978
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0xb88
-  __AUTH.__objc_data: 0x2000
+  __AUTH.__objc_data: 0x2050
   __AUTH.__data: 0x118
-  __DATA.__objc_ivar: 0x71c
+  __DATA.__objc_ivar: 0x720
   __DATA.__data: 0x1660
   __DATA.__bss: 0x648
   __DATA.__common: 0x270

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2870
-  Symbols:   5976
-  CStrings:  1789
+  Functions: 2880
+  Symbols:   5998
+  CStrings:  1792
 
Symbols:
+ +[SiriRaiseToSpeakContext supportsSecureCoding]
+ -[SASActivationRequest initWithRaiseToSpeakContext:]
+ -[SASActivationRequest isRaiseToSpeakRequest]
+ -[SiriActivationService activationRequestFromRaiseToSpeakWithContext:]
+ -[SiriRaiseToSpeakContext .cxx_destruct]
+ -[SiriRaiseToSpeakContext encodeWithCoder:]
+ -[SiriRaiseToSpeakContext initWithCoder:]
+ -[SiriRaiseToSpeakContext initWithRequestInfo:]
+ -[SiriRaiseToSpeakContext requestInfo]
+ -[SiriRaiseToSpeakContext speechRequestOptions]
+ GCC_except_table105
+ GCC_except_table163
+ GCC_except_table79
+ GCC_except_table99
+ _OBJC_CLASS_$_SiriRaiseToSpeakContext
+ _OBJC_IVAR_$_SiriRaiseToSpeakContext._requestInfo
+ _OBJC_METACLASS_$_SiriRaiseToSpeakContext
+ __OBJC_$_CLASS_METHODS_SiriRaiseToSpeakContext
+ __OBJC_$_INSTANCE_METHODS_SiriRaiseToSpeakContext
+ __OBJC_$_INSTANCE_VARIABLES_SiriRaiseToSpeakContext
+ __OBJC_$_PROP_LIST_SiriRaiseToSpeakContext
+ __OBJC_CLASS_RO_$_SiriRaiseToSpeakContext
+ __OBJC_METACLASS_RO_$_SiriRaiseToSpeakContext
+ _objc_msgSend$activationRequestFromRaiseToSpeakWithContext:
+ _objc_msgSend$initWithRaiseToSpeakContext:
+ _objc_msgSend$isRaiseToSpeakRequest
- GCC_except_table103
- GCC_except_table162
- GCC_except_table78
- GCC_except_table98
CStrings:
+ "%s #activation Rejecting VT/RTS activation request since we have a Starting presentation"
+ "%s #activation activationRequestFromRaiseToSpeakWithContext"
+ "-[SiriActivationService activationRequestFromRaiseToSpeakWithContext:]"
+ "SiriActivationEventTypeRaiseToSpeak"
- "%s #activation Rejecting VT/RTS activation request since we have a Starting or Active presentation"
```
