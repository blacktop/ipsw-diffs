## MobileTimer

> `/System/Library/PrivateFrameworks/MobileTimer.framework/MobileTimer`

```diff

-2303.2.2.0.0
-  __TEXT.__text: 0x10c2c0
+2303.2.4.0.0
+  __TEXT.__text: 0x10c468
   __TEXT.__auth_stubs: 0x1920
-  __TEXT.__objc_methlist: 0xd95c
-  __TEXT.__const: 0x1730
-  __TEXT.__oslogstring: 0x110b3
-  __TEXT.__cstring: 0x9836
+  __TEXT.__objc_methlist: 0xd98c
+  __TEXT.__const: 0x1750
+  __TEXT.__oslogstring: 0x110c3
+  __TEXT.__cstring: 0x9826
   __TEXT.__gcc_except_tab: 0x14a8
-  __TEXT.__dlopen_cstrs: 0x837
+  __TEXT.__dlopen_cstrs: 0x7e1
   __TEXT.__ustring: 0x1a
-  __TEXT.__swift5_typeref: 0xa18
+  __TEXT.__swift5_typeref: 0xa26
   __TEXT.__swift5_reflstr: 0x31d
   __TEXT.__swift5_assocty: 0x108
   __TEXT.__constg_swiftt: 0x610
   __TEXT.__swift5_fieldmd: 0x3b8
   __TEXT.__swift5_proto: 0x78
   __TEXT.__swift5_types: 0x74
-  __TEXT.__swift5_capture: 0x108c
+  __TEXT.__swift5_capture: 0x10bc
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift_as_entry: 0x120
+  __TEXT.__swift_as_entry: 0x124
   __TEXT.__swift_as_ret: 0x124
-  __TEXT.__unwind_info: 0x46d0
-  __TEXT.__eh_frame: 0x32d8
+  __TEXT.__unwind_info: 0x46f0
+  __TEXT.__eh_frame: 0x3300
   __TEXT.__objc_classname: 0x195a
-  __TEXT.__objc_methname: 0x1812f
+  __TEXT.__objc_methname: 0x181a0
   __TEXT.__objc_methtype: 0x42ac
-  __TEXT.__objc_stubs: 0x11e40
+  __TEXT.__objc_stubs: 0x11e80
   __DATA_CONST.__got: 0xc78
-  __DATA_CONST.__const: 0x4318
+  __DATA_CONST.__const: 0x4300
   __DATA_CONST.__objc_classlist: 0x6a0
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x370
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x60e8
+  __DATA_CONST.__objc_selrefs: 0x6100
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x420
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0xca0
-  __AUTH_CONST.__const: 0x3ce8
-  __AUTH_CONST.__cfstring: 0x7000
-  __AUTH_CONST.__objc_const: 0x29090
+  __AUTH_CONST.__const: 0x3d60
+  __AUTH_CONST.__cfstring: 0x6fe0
+  __AUTH_CONST.__objc_const: 0x290a8
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_floatobj: 0x10

   __DATA.__objc_ivar: 0x96c
   __DATA.__data: 0x2ba8
   __DATA.__common: 0x68
-  __DATA.__bss: 0x13a0
+  __DATA.__bss: 0x1390
   __DATA_DIRTY.__objc_data: 0x18b0
   __DATA_DIRTY.__bss: 0x288
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: BE20C531-4E54-3E51-9384-54C84710D72A
-  Functions: 6723
-  Symbols:   18463
-  CStrings:  8434
+  UUID: 8A6D30E8-FCE9-3CD2-B3D7-B5EAB22FA2BD
+  Functions: 6734
+  Symbols:   18470
+  CStrings:  8435
 
Symbols:
+ +[MTUtilities hasBeenUnlockedSinceBoot]
+ +[MTUtilities hasBeenUnlockedSinceBoot].cold.1
+ +[MTUtilities hasBeenUnlockedSinceBoot].cold.2
+ -[MTTimerDurationManager initWithPersistence:defaultsRestore:]
+ -[MTTimerStorage store_waitForPendingTasksWithCompletion:]
+ GCC_except_table114
+ _MobileKeyBagLibrary
+ _MobileKeyBagLibrary.cold.1
+ __OBJC_$_CLASS_PROP_LIST_MTUtilities
+ __OBJC_$_PROP_LIST_MTTimerStorage.362
+ ___block_descriptor_73_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ _block_copy_helper.1016
+ _block_copy_helper.772
+ _block_copy_helper.783
+ _block_copy_helper.795
+ _block_copy_helper.807
+ _block_copy_helper.819
+ _block_copy_helper.831
+ _block_copy_helper.843
+ _block_copy_helper.855
+ _block_copy_helper.867
+ _block_copy_helper.879
+ _block_copy_helper.891
+ _block_copy_helper.903
+ _block_copy_helper.915
+ _block_copy_helper.927
+ _block_copy_helper.939
+ _block_copy_helper.951
+ _block_copy_helper.963
+ _block_copy_helper.975
+ _block_copy_helper.987
+ _block_copy_helper.999
+ _block_descriptor.1001
+ _block_descriptor.1018
+ _block_descriptor.774
+ _block_descriptor.785
+ _block_descriptor.797
+ _block_descriptor.809
+ _block_descriptor.821
+ _block_descriptor.833
+ _block_descriptor.845
+ _block_descriptor.857
+ _block_descriptor.869
+ _block_descriptor.881
+ _block_descriptor.893
+ _block_descriptor.905
+ _block_descriptor.917
+ _block_descriptor.929
+ _block_descriptor.941
+ _block_descriptor.953
+ _block_descriptor.965
+ _block_descriptor.977
+ _block_descriptor.989
+ _block_destroy_helper.1000
+ _block_destroy_helper.1017
+ _block_destroy_helper.773
+ _block_destroy_helper.784
+ _block_destroy_helper.796
+ _block_destroy_helper.808
+ _block_destroy_helper.820
+ _block_destroy_helper.832
+ _block_destroy_helper.844
+ _block_destroy_helper.856
+ _block_destroy_helper.868
+ _block_destroy_helper.880
+ _block_destroy_helper.892
+ _block_destroy_helper.904
+ _block_destroy_helper.916
+ _block_destroy_helper.928
+ _block_destroy_helper.940
+ _block_destroy_helper.952
+ _block_destroy_helper.964
+ _block_destroy_helper.976
+ _block_destroy_helper.988
+ _objc_msgSend$initWithPersistence:defaultsRestore:
+ _objc_msgSend$waitForPendingTasksWithCompletion:
+ _objectdestroy.327Tm
+ _objectdestroy.360Tm
+ _objectdestroy.368Tm
+ _objectdestroy.420Tm
+ _symbolic Iegh_
+ _symbolic IeyBh_
- +[MTDeviceListener _latestKeyBagValueForHasBeenUnlockedSinceBoot].cold.1
- +[MTDeviceListener _latestKeyBagValueForHasBeenUnlockedSinceBoot].cold.2
- GCC_except_table10
- GCC_except_table21
- __OBJC_$_PROP_LIST_MTTimerStorage.361
- ___block_descriptor_65_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___getMKBDeviceUnlockedSinceBootSymbolLoc_block_invoke.cold.1
- ___getMKBGetDeviceLockStateSymbolLoc_block_invoke.cold.1
- _block_copy_helper.1002
- _block_copy_helper.758
- _block_copy_helper.769
- _block_copy_helper.781
- _block_copy_helper.793
- _block_copy_helper.805
- _block_copy_helper.817
- _block_copy_helper.829
- _block_copy_helper.841
- _block_copy_helper.853
- _block_copy_helper.865
- _block_copy_helper.877
- _block_copy_helper.889
- _block_copy_helper.901
- _block_copy_helper.913
- _block_copy_helper.925
- _block_copy_helper.937
- _block_copy_helper.949
- _block_copy_helper.961
- _block_copy_helper.973
- _block_copy_helper.985
- _block_descriptor.1004
- _block_descriptor.760
- _block_descriptor.771
- _block_descriptor.783
- _block_descriptor.795
- _block_descriptor.807
- _block_descriptor.819
- _block_descriptor.831
- _block_descriptor.843
- _block_descriptor.855
- _block_descriptor.867
- _block_descriptor.879
- _block_descriptor.891
- _block_descriptor.903
- _block_descriptor.915
- _block_descriptor.927
- _block_descriptor.939
- _block_descriptor.951
- _block_descriptor.963
- _block_descriptor.975
- _block_descriptor.987
- _block_destroy_helper.1003
- _block_destroy_helper.759
- _block_destroy_helper.770
- _block_destroy_helper.782
- _block_destroy_helper.794
- _block_destroy_helper.806
- _block_destroy_helper.818
- _block_destroy_helper.830
- _block_destroy_helper.842
- _block_destroy_helper.854
- _block_destroy_helper.866
- _block_destroy_helper.878
- _block_destroy_helper.890
- _block_destroy_helper.902
- _block_destroy_helper.914
- _block_destroy_helper.926
- _block_destroy_helper.938
- _block_destroy_helper.950
- _block_destroy_helper.962
- _block_destroy_helper.974
- _block_destroy_helper.986
- _objectdestroy.321Tm
- _objectdestroy.354Tm
- _objectdestroy.362Tm
- _objectdestroy.414Tm
CStrings:
+ "%{public}@ initWithPersistence defaultsRestore: %i"
+ "initWithPersistence:defaultsRestore:"
+ "store_waitForPendingTasksWithCompletion:"
+ "waitForPendingTasksWithCompletion:"
- "%{public}@ initWithPersistence"
- "MTDeviceListener.m"

```
