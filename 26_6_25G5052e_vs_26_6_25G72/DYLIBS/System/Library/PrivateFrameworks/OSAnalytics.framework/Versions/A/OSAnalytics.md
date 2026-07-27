## OSAnalytics

> `/System/Library/PrivateFrameworks/OSAnalytics.framework/Versions/A/OSAnalytics`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__got`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-934.160.3.0.0
-  __TEXT.__text: 0x4c0fc
+934.160.4.0.0
+  __TEXT.__text: 0x4c1e0
   __TEXT.__auth_stubs: 0x1910
   __TEXT.__objc_methlist: 0x1c40
   __TEXT.__oslogstring: 0x388c
-  __TEXT.__cstring: 0x8e16
+  __TEXT.__cstring: 0x8e06
   __TEXT.__const: 0x718
   __TEXT.__gcc_except_tab: 0x10cc
   __TEXT.__dlopen_cstrs: 0x1a9

   __TEXT.__objc_methtype: 0xc4d
   __TEXT.__objc_stubs: 0x4760
   __DATA_CONST.__got: 0x438
-  __DATA_CONST.__const: 0x900
+  __DATA_CONST.__const: 0x8b8
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10

   __DATA_CONST.__objc_arraydata: 0x8f0
   __AUTH_CONST.__auth_got: 0xc98
   __AUTH_CONST.__const: 0x1088
-  __AUTH_CONST.__cfstring: 0x9960
+  __AUTH_CONST.__cfstring: 0x9920
   __AUTH_CONST.__objc_const: 0x38d0
   __AUTH_CONST.__objc_intobj: 0x4b0
   __AUTH_CONST.__objc_dictobj: 0x500

   - /usr/lib/swift/libswiftos.dylib
   Functions: 1235
   Symbols:   2654
-  CStrings:  2897
+  CStrings:  2895
 
Functions:
~ -[OSAProxyConfiguration isFile:validForSubmission:reasonableSize:to:internalTypes:result:] : 2292 -> 2208
~ ___40-[OSASystemConfiguration sysVersionData]_block_invoke : 672 -> 688
~ +[OSASystemConfiguration fastLane] : 240 -> 252
~ +[OSASystemConfiguration(optIn) boolValueForCRSSetting:] : 692 -> 704
~ _rtcsc_send_base : 636 -> 908
CStrings:
+ "GM"
- "%@-seed"
- "Seed"
- "seed"
```
