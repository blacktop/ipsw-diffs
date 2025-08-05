## MusicKit

> `/System/Library/Frameworks/MusicKit.framework/MusicKit`

```diff

-4025.100.87.0.0
-  __TEXT.__text: 0x5014b0
-  __TEXT.__auth_stubs: 0x2ec0
+4025.100.93.0.0
+  __TEXT.__text: 0x507918
+  __TEXT.__auth_stubs: 0x2ed0
   __TEXT.__objc_methlist: 0x206c
-  __TEXT.__const: 0x474b4
+  __TEXT.__const: 0x47514
   __TEXT.__gcc_except_tab: 0x1fdc
-  __TEXT.__cstring: 0x11ab7
+  __TEXT.__cstring: 0x11bb7
   __TEXT.__dlopen_cstrs: 0xa32
-  __TEXT.__oslogstring: 0x1273
-  __TEXT.__swift5_typeref: 0x109aa
-  __TEXT.__swift5_reflstr: 0xb2f9
+  __TEXT.__oslogstring: 0x17d3
+  __TEXT.__swift5_typeref: 0x109da
+  __TEXT.__swift5_reflstr: 0xb349
   __TEXT.__swift5_assocty: 0x2e40
-  __TEXT.__constg_swiftt: 0xb390
+  __TEXT.__constg_swiftt: 0xb398
   __TEXT.__swift5_builtin: 0x320
-  __TEXT.__swift5_fieldmd: 0xd92c
-  __TEXT.__swift5_capture: 0x493c
+  __TEXT.__swift5_fieldmd: 0xd950
+  __TEXT.__swift5_capture: 0x4994
   __TEXT.__swift5_proto: 0x400c
   __TEXT.__swift5_types: 0xe98
   __TEXT.__swift_as_entry: 0xac0
-  __TEXT.__swift_as_ret: 0xe90
+  __TEXT.__swift_as_ret: 0xe94
   __TEXT.__swift5_protos: 0x1e0
   __TEXT.__swift5_mpenum: 0x1dc
   __TEXT.__lldbsummaries: 0x34
-  __TEXT.__unwind_info: 0x15fc0
-  __TEXT.__eh_frame: 0x25880
+  __TEXT.__unwind_info: 0x160f0
+  __TEXT.__eh_frame: 0x258e4
   __TEXT.__objc_classname: 0xba0
   __TEXT.__objc_methname: 0x6a05
   __TEXT.__objc_methtype: 0xec2
   __TEXT.__objc_stubs: 0x4240
-  __DATA_CONST.__got: 0x930
+  __DATA_CONST.__got: 0x938
   __DATA_CONST.__const: 0x1528
   __DATA_CONST.__objc_classlist: 0x2f8
   __DATA_CONST.__objc_catlist: 0x18

   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x158
   __DATA_CONST.__objc_arraydata: 0x168
-  __AUTH_CONST.__auth_got: 0x1770
-  __AUTH_CONST.__const: 0x25d50
+  __AUTH_CONST.__auth_got: 0x1778
+  __AUTH_CONST.__const: 0x27d78
   __AUTH_CONST.__cfstring: 0xc80
   __AUTH_CONST.__objc_const: 0x6ad0
   __AUTH_CONST.__objc_doubleobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_intobj: 0x78
-  __AUTH.__objc_data: 0x6e8
-  __AUTH.__data: 0x39a8
+  __AUTH.__objc_data: 0x698
+  __AUTH.__data: 0x37d8
   __DATA.__objc_ivar: 0x154
-  __DATA.__data: 0x96a8
-  __DATA.__bss: 0x5db80
-  __DATA.__common: 0x138
-  __DATA_DIRTY.__objc_data: 0xce8
-  __DATA_DIRTY.__data: 0xa9d1
-  __DATA_DIRTY.__bss: 0x14360
-  __DATA_DIRTY.__common: 0xa20
+  __DATA.__data: 0x9418
+  __DATA.__bss: 0x5c370
+  __DATA.__common: 0x128
+  __DATA_DIRTY.__objc_data: 0xd38
+  __DATA_DIRTY.__data: 0xae71
+  __DATA_DIRTY.__bss: 0x15b98
+  __DATA_DIRTY.__common: 0xa48
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D3737127-AE8B-33CF-9212-B23E56832174
-  Functions: 39183
-  Symbols:   33950
-  CStrings:  3150
+  UUID: 364F6D75-1871-3009-8369-8FDB0832A57F
+  Functions: 39416
+  Symbols:   34198
+  CStrings:  3172
 
Symbols:
+ _objectdestroy.25Tm
+ _objectdestroy.391Tm
+ _objectdestroy.60Tm
+ _symbolic ScTySSSg______pGSg s5ErrorP
+ _symbolic ______p 8MusicKit0A14LibraryAddableP
+ _symbolic ______pSg 8MusicKit0A14LibraryAddableP
+ _symbolic _____y__________G 8MusicKit0A17AttributePropertyC AA0A5VideoV AA0A13IdentifierSetV
+ _symbolic _____y__________G 8MusicKit0A17AttributePropertyC AA4SongV AA0A13IdentifierSetV
- _objectdestroy.23Tm
- _objectdestroy.388Tm
- _objectdestroy.40Tm
- _objectdestroy.41Tm
- _symbolic _____ySSSg______pGSg s6ResultOsRi_zRi0_zrlE s5ErrorP
CStrings:
+ "%s Album<%{public}s> has cleanDownloadedTrackCount=%{public}ld."
+ "%s Album<%{public}s> has cleanTrackCount=%{public}ld."
+ "%s Album<%{public}s> has no clean track count or tracks loaded, deferring to container's `hasExplicitContent` value."
+ "%s Album<%{public}s> has tracks fully loaded, returning %{bool}d."
+ "%s Album<%{public}s> tracks not fully loaded and loaded tracks are all `ContentRating.explicit`, deferring to container's `hasExplicitContent` value."
+ "%s Album<%{public}s> tracks not fully loaded, but has at least one `ContentRating.clean` track."
+ "%s Album<%{public}s> tracks not fully loaded, but has at least one downloaded+`ContentRating.clean` track."
+ "%s Playlist<%{public}s> has hasCleanDownloadedTracks=%{bool,public}d."
+ "%s Playlist<%{public}s> has hasCleanTracks=%{bool,public}d."
+ "%s Playlist<%{public}s> has no clean track count or tracks loaded, deferring to container's `hasExplicitContent` value."
+ "%s Playlist<%{public}s> has tracks fully loaded, returning %{bool}d."
+ "%s Playlist<%{public}s> tracks not fully loaded and loaded tracks are all `ContentRating.explicit`, deferring to container's `hasExplicitContent` value."
+ "%s Playlist<%{public}s> tracks not fully loaded, but has at least one `ContentRating.clean` track."
+ "%s Playlist<%{public}s> tracks not fully loaded, but has at least one downloaded+`ContentRating.clean` track."
+ ".cellularNetwork"
+ ".constrainedNetwork"
+ ".deviceNotCharging"
+ ".expensiveNetwork"
+ ".poorNetworkQuality"
+ ".thermalPressure"
+ ".waitingForRetry"
+ "Fetching preferred language tag for %{public}s..."
+ "Unable to get preferred language tag for %{public}s: %{public}@."
+ "albumIdentifierSet"
+ "task"
- "%s Album<%{public}s> has no cleanDownloadedTrackCount, deferring to container's `hasExplicitContent` value."
- "%s Album<%{public}s> has no tracks, deferring to container's `hasExplicitContent` value."
- "result"

```
