## ASIOKit

> `/System/Library/Extensions/ASIOKit.kext/ASIOKit`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__got`

```diff

-27.2.2.0.0
-  __TEXT.__cstring: 0x261
-  __TEXT.__const: 0x8580
-  __TEXT_EXEC.__text: 0x3cfdc
-  __TEXT_EXEC.__auth_stubs: 0x210
+27.2.6.0.0
+  __TEXT.__cstring: 0xd2
+  __TEXT.__const: 0x91d0
+  __TEXT_EXEC.__text: 0x50a40
+  __TEXT_EXEC.__auth_stubs: 0x1f0
   __DATA.__data: 0x158
   __DATA.__common: 0x60
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x2be8
+  __DATA_CONST.__const: 0x34c0
   __DATA_CONST.__kalloc_type: 0x80
-  __DATA_CONST.__auth_got: 0x108
+  __DATA_CONST.__auth_got: 0xf8
   __DATA_CONST.__got: 0x58
   Functions: 97
-  Symbols:   352
-  CStrings:  18
+  Symbols:   349
+  CStrings:  11
 
Symbols:
+ __ZN7ASIOKit8teardownEv
- __ZN7ASIOKit16DqycVGt64ff4YTONEP11_baaOptions
- __ZN7ASIOKit16kKcutC1yTbOdNEHiEP11_baaOptions
- __ZN7OSArray12withCapacityEj
- __ZN8OSString11withCStringEPKc
CStrings:
+ "1211111212221212111"
- "1.2.840.113635.100.10.1"
- "1.2.840.113635.100.8.3"
- "1.2.840.113635.100.8.4"
- "1.2.840.113635.100.8.5"
- "1.2.840.113635.100.8.6"
- "1.2.840.113635.100.8.7"
- "121111121222121211"
- "{\"kMAOptionsBAAValidity\": 525600, \"kMAOptionsBAAOIDSToInclude\": [\"1.2.840.113635.100.10.1\", \"1.2.840.113635.100.8.3\", \"1.2.840.113635.100.8.4\", \"1.2.840.113635.100.8.5\", \"1.2.840.113635.100.8.6\", \"1.2.840.113635.100.8.7\"], \"kMAOptionsBAASCRTAttestation\": true}"
```
