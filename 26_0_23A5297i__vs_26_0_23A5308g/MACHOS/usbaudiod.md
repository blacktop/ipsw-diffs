## usbaudiod

> `/System/Library/Audio/Plug-Ins/usbaudio.bundle/usbaudiod`

```diff

-802.45.0.0.0
-  __TEXT.__text: 0x115158
-  __TEXT.__auth_stubs: 0x1a00
+802.55.0.0.0
+  __TEXT.__text: 0x116030
+  __TEXT.__auth_stubs: 0x1a10
   __TEXT.__objc_stubs: 0x220
   __TEXT.__init_offsets: 0x8
   __TEXT.__objc_methlist: 0x804
-  __TEXT.__const: 0xbaf2
-  __TEXT.__cstring: 0x8012
-  __TEXT.__swift5_typeref: 0x2d46
+  __TEXT.__const: 0xbb02
+  __TEXT.__cstring: 0x80a2
+  __TEXT.__swift5_typeref: 0x2d6e
   __TEXT.__swift5_entry: 0x8
   __TEXT.__gcc_except_tab: 0x2f4
-  __TEXT.__objc_classname: 0x81
+  __TEXT.__objc_classname: 0xae
   __TEXT.__objc_methname: 0x1886
   __TEXT.__objc_methtype: 0x7fd
   __TEXT.__oslogstring: 0x298
-  __TEXT.__constg_swiftt: 0x5144
-  __TEXT.__swift5_reflstr: 0x51d6
-  __TEXT.__swift5_fieldmd: 0x6670
+  __TEXT.__constg_swiftt: 0x516c
+  __TEXT.__swift5_reflstr: 0x51e6
+  __TEXT.__swift5_fieldmd: 0x6688
   __TEXT.__swift5_builtin: 0xdac
   __TEXT.__swift5_assocty: 0x210
-  __TEXT.__swift5_capture: 0xc54
+  __TEXT.__swift5_capture: 0xc64
   __TEXT.__swift5_proto: 0x964
   __TEXT.__swift5_types: 0x524
   __TEXT.__swift5_protos: 0x44
   __TEXT.__swift5_mpenum: 0x4c
   __TEXT.__swift_as_entry: 0x4
   __TEXT.__swift_as_ret: 0x8
-  __TEXT.__unwind_info: 0x3710
-  __TEXT.__eh_frame: 0x5d20
-  __DATA_CONST.__auth_got: 0xd10
-  __DATA_CONST.__got: 0x3e8
+  __TEXT.__unwind_info: 0x3730
+  __TEXT.__eh_frame: 0x5d58
+  __DATA_CONST.__auth_got: 0xd18
+  __DATA_CONST.__got: 0x3f0
   __DATA_CONST.__auth_ptr: 0xaf8
-  __DATA_CONST.__const: 0xded8
+  __DATA_CONST.__const: 0xdfb0
   __DATA_CONST.__cfstring: 0xe0
   __DATA_CONST.__objc_classlist: 0x230
-  __DATA_CONST.__objc_protolist: 0x20
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA.__objc_const: 0x4e20
+  __DATA.__objc_const: 0x4e70
   __DATA.__objc_selrefs: 0x840
   __DATA.__objc_ivar: 0x68
-  __DATA.__objc_data: 0x2548
-  __DATA.__data: 0x56e8
+  __DATA.__objc_data: 0x2578
+  __DATA.__data: 0x57b8
   __DATA.__common: 0x1f8
   __DATA.__bss: 0x115e0
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDarwin.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 0AF3F3B5-0115-3E12-A964-15A42AAD5832
-  Functions: 5000
-  Symbols:   669
-  CStrings:  1288
+  UUID: 9CF97A0D-0E34-3A63-9E14-6750BF1DFD00
+  Functions: 5008
+  Symbols:   673
+  CStrings:  1296
 
Symbols:
+ _$sSo18OS_dispatch_sourceC8DispatchE16makeSignalSource6signal5queueSo0a1_b1_c1_H0_ps5Int32V_So0a1_b1_I0CSgtFZ
+ _$sSo18OS_dispatch_sourceP8DispatchE15setEventHandler3qos5flags7handleryAC0D3QoSV_AC0D13WorkItemFlagsVyyXBSgtF
+ _$sSo18OS_dispatch_sourceP8DispatchE6resumeyyF
+ _OBJC_CLASS_$_OS_dispatch_source
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private
- _$s6Darwin7SIG_DFLys5Int32VXCSgvg
- _signal
CStrings:
+ " error forcing alternate to 0: "
+ " forcing streaming alternates to 0"
+ ", using previous value"
+ "Feedback recieved frameStatus "
+ "Handling SIGTERM"
+ "Installing SIGTERM handler"
+ "OS_dispatch_source"
+ "OS_dispatch_source_signal"
+ "signalSource"
- "Feedback recieved frameStatus kIOReturnNotResponding, using previous value"

```
