## com.apple.filesystems.udf

> `com.apple.filesystems.udf`

```diff

-331.0.0.0.0
+331.40.5.0.0
   __TEXT.__const: 0x1b08
-  __TEXT.__cstring: 0x308d
-  __TEXT_EXEC.__text: 0x300c8
-  __TEXT_EXEC.__auth_stubs: 0xa40
+  __TEXT.__cstring: 0x307c
+  __TEXT_EXEC.__text: 0x301cc
+  __TEXT_EXEC.__auth_stubs: 0xa50
   __DATA.__data: 0x4f8
   __DATA.__common: 0x4d8
   __DATA.__bss: 0x1425
   __DATA_CONST.__const: 0x1140
-  __DATA_CONST.__kalloc_type: 0x80
   __DATA_CONST.__kalloc_var: 0xa0
-  __DATA_CONST.__auth_got: 0x520
+  __DATA_CONST.__auth_got: 0x528
   __DATA_CONST.__got: 0x20
   Functions: 860
-  Symbols:   1178
-  CStrings:  349
+  Symbols:   1177
+  CStrings:  348
 
Symbols:
+ _IOFreeDataShareable
+ _IOMallocDataShareable
+ _IOMallocZeroDataShareable
+ __ZZN8UDFMount11GetPartMapsEP26UDFLogicalVolumeDescriptorE20kalloc_type_view_459
+ __ZZN8UDFMount12FreePartMapsEvE20kalloc_type_view_288
- _IOFreeTypeImpl
- _IOMallocTypeImpl
- __ZZN8UDFMount11GetPartMapsEP26UDFLogicalVolumeDescriptorE20kalloc_type_view_450
- __ZZN8UDFMount12FreePartMapsEvE20kalloc_type_view_279
- __ZZN8UDFMount13SetDeviceInfoEiP5mountP5vnodeP14udf_mount_argsE20kalloc_type_view_250
- __ZZN8UDFMountD1EvE20kalloc_type_view_212
Functions:
~ __ZN8UDFMountD2Ev : 176 -> 168
~ __ZN8UDFMountD1Ev : 176 -> 168
~ __ZN8UDFMount13SetDeviceInfoEiP5mountP5vnodeP14udf_mount_args : 184 -> 180
~ __ZN8UDFMount12ReadDiscInfoEmP10CDDiscInfoP11vfs_context : 124 -> 232
~ __ZN8UDFMount10FreeExtentER14UDFLogicalAddrtjjPib : 428 -> 448
~ __ZN8UDFMount14NewReservationEtxPi : 68 -> 88
~ __ZN8UDFMount13ReserveBlocksEttjjPi : 228 -> 256
~ __ZN8UDFMount11AllocExtentEtjjPjS0_Pibj : 432 -> 452
~ __ZN7UDFNodeC2EP8UDFMountRK14UDFLogicalAddrjPKctxPhb : 552 -> 564
~ __ZN18UDFNamedStreamNodeC2EP8UDFMountRK14UDFLogicalAddrjP16UDFStreamDirNodePKctxPhb : 144 -> 152
~ __ZN12UDFAllocZoneC2Embiii : 240 -> 248
~ __ZN12UDFAllocZone8GrowZoneEm : 152 -> 168
~ __ZN12UDFAllocZoneD2Ev : 164 -> 184
~ __ZN12UDFAllocZoneD1Ev : 164 -> 184
CStrings:
- "site.CDTrackInfo"
```
