## thermalmonitord

> `/usr/libexec/thermalmonitord`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2087.60.5.0.0
-  __TEXT.__text: 0x51e28
-  __TEXT.__auth_stubs: 0x13e0
-  __TEXT.__objc_stubs: 0x4f20
-  __TEXT.__objc_methlist: 0x4014
+2087.60.6.0.0
+  __TEXT.__text: 0x527f4
+  __TEXT.__auth_stubs: 0x1420
+  __TEXT.__objc_stubs: 0x4f80
+  __TEXT.__objc_methlist: 0x4044
   __TEXT.__const: 0x1550
   __TEXT.__objc_classname: 0x1303
-  __TEXT.__objc_methtype: 0x1b05
-  __TEXT.__objc_methname: 0x838f
-  __TEXT.__cstring: 0x4df1
+  __TEXT.__objc_methtype: 0x1b2e
+  __TEXT.__objc_methname: 0x8430
+  __TEXT.__cstring: 0x4e1c
   __TEXT.__gcc_except_tab: 0x3ac
-  __TEXT.__oslogstring: 0x9de9
-  __TEXT.__unwind_info: 0x1b48
+  __TEXT.__oslogstring: 0xa09d
+  __TEXT.__unwind_info: 0x1b78
   __DATA_CONST.__const: 0x1458
-  __DATA_CONST.__cfstring: 0x6760
+  __DATA_CONST.__cfstring: 0x67a0
   __DATA_CONST.__objc_classlist: 0x520
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38

   __DATA_CONST.__objc_dictobj: 0x730
   __DATA_CONST.__objc_arrayobj: 0x228
   __DATA_CONST.__objc_doubleobj: 0x40
-  __DATA_CONST.__auth_got: 0xa08
+  __DATA_CONST.__auth_got: 0xa28
   __DATA_CONST.__got: 0x630
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA.__objc_const: 0xc928
-  __DATA.__objc_selrefs: 0x1990
-  __DATA.__objc_ivar: 0xa2c
+  __DATA.__objc_const: 0xc9a8
+  __DATA.__objc_selrefs: 0x19a8
+  __DATA.__objc_ivar: 0xa3c
   __DATA.__objc_data: 0x3340
   __DATA.__data: 0x370
   __DATA.__common: 0x9f6

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2001
-  Symbols:   417
-  CStrings:  3745
+  Functions: 2014
+  Symbols:   421
+  CStrings:  3766
 
Symbols:
+ _CFDataGetBytes
+ _IOObjectRetain
+ _IORegistryEntryGetName
+ _IORegistryEntryGetParentEntry
CStrings:
+ "<Error> %@: dieCount*loopCount %u exceeds the %d-bit TDDB cluster mask capacity"
+ "<Error> Failed to find %s service for die %u in the registry"
+ "<Error> Failed to find %s service(s) in the registry"
+ "<Error> Failed to read valid die/loop count for PMP index %u (die %u loop %u)"
+ "<Error> LTS invariant: PMP for die %u does not expose key %@ (die-namespace mismatch)"
+ "<Error> LTS invariant: PMP instance %u per-die loop-count %u != %u"
+ "<Error> LTS invariant: multi-PMP instance %u reports die-count %u (expected 1)"
+ "<Error> LTS: duplicate PMP index %d, ignoring"
+ "<Error> LTS: failed to find %s service(s) in the registry"
+ "<Error> LTS: no usable ApplePMPv2 instances found"
+ "<Error> LTS: skipping ApplePMPv2 with unusable pmpN index %d"
+ "<Error> LTS: unexpected type/size for PMP property"
+ "<Error> Unexpected aggregated die count %u (max %d)"
+ "<Notice> dieCount:%u loopCount:%u pmpServices:%u"
+ "B36@0:8^{__CFData=}16^{__CFString=}24I32"
+ "I20@0:8I16"
+ "^{__CFData=}32@0:8^{__CFString=}16B24I28"
+ "^{__CFString=}20@0:8I16"
+ "_pmpKeyNamespaceVerified"
+ "_pmpServiceCount"
+ "_pmpServices"
+ "_pmpServicesScouted"
+ "copyKeyFromPMP:is_64:forDie:"
+ "copyPmpDieProbeKeyForDie:"
+ "ensurePmpServices"
+ "lts-ctrl-%u-0-cores"
+ "lts-ctrl-%u-0-is-inuse"
+ "sendDataToPMP:forKey:forDie:"
+ "serviceForDie:"
+ "verifyPmpKeyNamespace:"
- "<Error> Failed to find %s service in the registry"
- "<Error> Failed to read die count for registry\n"
- "<Error> Failed to read loop count for registry\n"
- "<Notice> dieCount:%u loopCount:%u"
- "B32@0:8^{__CFData=}16^{__CFString=}24"
- "^{__CFData=}28@0:8^{__CFString=}16B24"
- "copyKeyFromPMP:is_64:"
- "getPMPSvc"
- "sendDataToPMP:forKey:"
```
