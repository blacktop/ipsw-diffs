## plutil

> `/usr/bin/plutil`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_entry`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`

```diff

-5027.0.63.2.0
-  __TEXT.__text: 0x1fb84
+5027.0.69.0.0
+  __TEXT.__text: 0x1fb60
   __TEXT.__auth_stubs: 0xbb0
   __TEXT.__objc_stubs: 0xf00
   __TEXT.__objc_methlist: 0x298
Symbols:
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Binaries/Foundation/install/TempContent/Objects/Foundation.build/plutil.build/Objects-normal/arm64e/PLUContext-9fbb4fb7b7a449a9cbab295f97fc2476.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Binaries/Foundation/install/TempContent/Objects/Foundation.build/plutil.build/Objects-normal/arm64e/PLUContext-a6c61091ef9b63668b80dab822da89b0.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Binaries/Foundation/install/TempContent/Objects/Foundation.build/plutil.build/Objects-normal/arm64e/PLUContext-275d7776adebe4fd526febab5ec36391.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Binaries/Foundation/install/TempContent/Objects/Foundation.build/plutil.build/Objects-normal/arm64e/PLUContext-b9f6f748e2d05774cdc42e134219874e.o
Functions:
~ _$s6plutil6_value9atKeyPath2in09remainingdE0ypSgSaySSG_yps10ArraySliceVySSGtF : 1312 -> 1300
~ _$s6plutil12_removeValue9atKeyPath2in09remainingeF0ypSgSaySSG_yps10ArraySliceVySSGtKF : 2716 -> 2708
~ _$s6plutil12_insertValue_9atKeyPath2in09remainingeF09replacing9appendingypyp_SaySSGyps10ArraySliceVySSGS2btKF : 4152 -> 4144
~ _$ss13_parseInteger5ascii5radixq_Sgx_SitSyRzs010FixedWidthB0R_r0_lFSSSiADSSRszsAER_r0_lIetgyr_Tpq5Si_Tg5 : 1444 -> 1436
```
