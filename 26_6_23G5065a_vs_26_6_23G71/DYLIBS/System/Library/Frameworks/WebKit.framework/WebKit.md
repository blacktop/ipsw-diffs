## WebKit

> `/System/Library/Frameworks/WebKit.framework/WebKit`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__oslogstring`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-624.4.5.10.3
-  __TEXT.__text: 0x138b398
+624.4.5.10.5
+  __TEXT.__text: 0x138b2e4
   __TEXT.__auth_stubs: 0x19fb0
   __TEXT.__delay_helper: 0xdc
   __TEXT.__objc_methlist: 0x1aa74

   __TEXT.__gcc_except_tab: 0x79608
   __TEXT.__oslogstring: 0x5c39d
   __TEXT.__ustring: 0xddc
-  __TEXT.__unwind_info: 0x2e098
+  __TEXT.__unwind_info: 0x2e0a0
   __TEXT.__eh_frame: 0x2490
   __TEXT.__objc_classname: 0x37b2
   __TEXT.__objc_methname: 0x4c5ac
Functions:
~ __ZN6WebKit10WebProcess30ensureNetworkProcessConnectionEv : 2392 -> 2372
~ __ZN6WebKit10WebProcess30registerURLSchemeAsCORSEnabledERKN3WTF6StringE : 260 -> 212
~ __ZN3IPC10Connection4sendIN8Messages29NetworkConnectionToWebProcess31RegisterURLSchemesAsCORSEnabledEEENS_5ErrorEOT_yN3WTF9OptionSetINS_10SendOptionELNS8_14ConcurrencyTagE0EEENSt3__18optionalINS8_6Thread3QOSEEE : 160 -> 128
~ __ZN6WebKit7WebPage24registerURLSchemeHandlerEN3WTF23ObjectIdentifierGenericINS_33WebURLSchemeHandlerIdentifierTypeENS1_38ObjectIdentifierMainThreadAccessTraitsIyEEyEERKNS1_6StringE : 1332 -> 1252
```
