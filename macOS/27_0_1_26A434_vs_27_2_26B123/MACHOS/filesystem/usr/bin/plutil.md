## plutil

> `/usr/bin/plutil`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`

```diff

-5027.0.69.0.0
-  __TEXT.__text: 0x1f4f8
+5027.1.8.0.0
+  __TEXT.__text: 0x1f518
   __TEXT.__auth_stubs: 0xbb0
   __TEXT.__objc_stubs: 0xf00
   __TEXT.__objc_methlist: 0x298

   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__info_plist: 0x54e
+  __TEXT.__info_plist: 0x54d
   __TEXT.__unwind_info: 0x4f0
   __TEXT.__eh_frame: 0x830
   __DATA_CONST.__const: 0xcd8
Symbols:
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Binaries/Foundation/install/TempContent/Objects/Foundation.build/plutil.build/Objects-normal/arm64e/PLUContext-5f1f763ca5760233b3fd545c03da1a4c.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Binaries/Foundation/install/TempContent/Objects/Foundation.build/plutil.build/Objects-normal/arm64e/PLUContext-c01be6db0999b5c5cafcdc2f7f3a910d.o
+ _$sSMsSkRzrlE4sort2byySb7ElementSTQz_ADtKXE_tKFySryADGzKXEfU_s15ContiguousArrayVySSG_Tg5
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Binaries/Foundation/install/TempContent/Objects/Foundation.build/plutil.build/Objects-normal/arm64e/PLUContext-6b0d9e4b920eacfd24df6453b8d8f677.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Binaries/Foundation/install/TempContent/Objects/Foundation.build/plutil.build/Objects-normal/arm64e/PLUContext-85fe1b2ef7813111b9832035a4d17f97.o
- _$sSr15_stableSortImpl2byySbx_xtKXE_tKFSS_Tg5
Functions:
~ _$s6plutil33_swiftLiteralDataWithPropertyList33_EB6C302B92FDEB1088B3414E11C53718LL_5depth6indent16originalFilenameSSyp_SiSbSStKF : 4792 -> 4796
~ _$s6plutil32_objcLiteralDataWithPropertyList33_EB6C302B92FDEB1088B3414E11C53718LL_5depth6indent16originalFilename06outputR0SSyp_SiSbS2StKF : 2212 -> 2216
~ _$sSr15_stableSortImpl2byySbx_xtKXE_tKFSS_Tg5 -> _$sSMsSkRzrlE4sort2byySb7ElementSTQz_ADtKXE_tKFySryADGzKXEfU_s15ContiguousArrayVySSG_Tg5 : 264 -> 276
~ _$s6plutil12PrintCommandV06prettyB0_6indent7spacingSSyp_S2itKF : 4224 -> 4228
~ _$s6plutil25rawStringWithPropertyListySSypKF : 1412 -> 1420
```
