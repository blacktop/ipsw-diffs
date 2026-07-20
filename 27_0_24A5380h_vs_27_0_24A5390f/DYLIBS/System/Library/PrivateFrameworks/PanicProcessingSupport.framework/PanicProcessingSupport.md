## PanicProcessingSupport

> `/System/Library/PrivateFrameworks/PanicProcessingSupport.framework/PanicProcessingSupport`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-34.0.0.0.0
-  __TEXT.__text: 0xcb5c
+37.0.0.0.0
+  __TEXT.__text: 0xc9f8
   __TEXT.__objc_methlist: 0x82c
   __TEXT.__const: 0x188
-  __TEXT.__cstring: 0x15ba
+  __TEXT.__cstring: 0x155a
   __TEXT.__oslogstring: 0xb85
   __TEXT.__gcc_except_tab: 0x124
   __TEXT.__swift5_typeref: 0x66

   __DATA_CONST.__objc_selrefs: 0x6d0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x38
-  __DATA_CONST.__objc_arraydata: 0x170
+  __DATA_CONST.__objc_arraydata: 0x148
   __DATA_CONST.__got: 0x1c8
   __AUTH_CONST.__const: 0x98
-  __AUTH_CONST.__cfstring: 0x2180
+  __AUTH_CONST.__cfstring: 0x20e0
   __AUTH_CONST.__objc_const: 0x1138
-  __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__auth_got: 0x4b8

   - /usr/lib/swift/libswiftos.dylib
   Functions: 270
   Symbols:   577
-  CStrings:  344
+  CStrings:  339
 
Symbols:
+ -[PanicReport setPlaneMetadata:]
+ _OBJC_IVAR_$_PanicReport._planeMetadata
- -[PanicReport setEnsembleMetadata:]
- _OBJC_IVAR_$_PanicReport._ensembleMetadata
Functions:
~ -[PanicReport setEnsembleMetadata:] -> -[PanicReport setPlaneMetadata:] : 620 -> 264
CStrings:
+ "plane_node"
+ "plane_supervisor"
- "chassisID"
- "ensembleID"
- "ensemble_node"
- "ensemble_supervisor"
- "totalNodeNumber"
- "totalReportNumber"
- "unique_crash_event_id"
```
