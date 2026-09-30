## AVConference

> `/System/Library/PrivateFrameworks/AVConference.framework/AVConference`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__cstring`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__auth_got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

 2215.5.1.0.0
-  __TEXT.__text: 0x740b44
+  __TEXT.__text: 0x740b20
   __TEXT.__auth_stubs: 0x5640
   __TEXT.__objc_methlist: 0x35e28
   __TEXT.__const: 0xbf40
   __TEXT.__cstring: 0x90a87
-  __TEXT.__oslogstring: 0x11815e
+  __TEXT.__oslogstring: 0x118156
   __TEXT.__gcc_except_tab: 0x2b48
   __TEXT.__ustring: 0x2d4
   __TEXT.__unwind_info: 0x10af0
   __TEXT.__objc_classname: 0x4ed7
   __TEXT.__objc_methname: 0x7e60e
   __TEXT.__objc_methtype: 0x284ce
-  __TEXT.__objc_stubs: 0x4f2e0
+  __TEXT.__objc_stubs: 0x4f2a0
   __DATA_CONST.__got: 0x1a60
   __DATA_CONST.__const: 0x6bc0
   __DATA_CONST.__objc_classlist: 0x12f0

   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
   Functions: 32308
-  Symbols:   48768
+  Symbols:   48766
   CStrings:  52107
 
Symbols:
- _objc_msgSend$setupLocalABTestSwitches
- _objc_msgSend$setupLocalOnOffSwitches
Functions:
~ -[VCSwitchManager initializeLocalSwitches] : 508 -> 472
CStrings:
+ " [%s] %s:%d SwitchManager: Non-seed build - using master local switch: %08X"
- " [%s] %s:%d SwitchManager: A/B testing turned off - using master local switch: %08X"
```
