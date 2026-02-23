## libsystem_containermanager.dylib

> `/usr/lib/system/libsystem_containermanager.dylib`

```diff

-725.100.34.0.0
-  __TEXT.__text: 0x2d800
+725.100.37.0.0
+  __TEXT.__text: 0x2d8c4
   __TEXT.__auth_stubs: 0xb70
   __TEXT.__const: 0x280
   __TEXT.__cstring: 0x3a63
-  __TEXT.__oslogstring: 0x4f32
+  __TEXT.__oslogstring: 0x4fc0
   __TEXT.__unwind_info: 0x688
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__const: 0x1c40

   - /usr/lib/system/libsystem_sandbox.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: 243CE960-08A0-3293-87D5-22345DAD95AE
+  UUID: 5E018F41-E89A-3CFB-8D8A-CD864F424E53
   Functions: 588
   Symbols:   1289
-  CStrings:  892
+  CStrings:  893
 
Symbols:
+ ___block_descriptor_tmp.1.1009
+ ___block_descriptor_tmp.1.725
+ ___block_descriptor_tmp.1.762
+ ___block_descriptor_tmp.1.969
+ ___block_descriptor_tmp.10.1062
+ ___block_descriptor_tmp.10.903
+ ___block_descriptor_tmp.1004
+ ___block_descriptor_tmp.1032
+ ___block_descriptor_tmp.11.1063
+ ___block_descriptor_tmp.12.1064
+ ___block_descriptor_tmp.12.896
+ ___block_descriptor_tmp.13.1069
+ ___block_descriptor_tmp.17.1073
+ ___block_descriptor_tmp.17.959
+ ___block_descriptor_tmp.2.728
+ ___block_descriptor_tmp.2.767
+ ___block_descriptor_tmp.2.895
+ ___block_descriptor_tmp.2.973
+ ___block_descriptor_tmp.26.1082
+ ___block_descriptor_tmp.28.1085
+ ___block_descriptor_tmp.3.730
+ ___block_descriptor_tmp.3.768
+ ___block_descriptor_tmp.3.788
+ ___block_descriptor_tmp.3.905
+ ___block_descriptor_tmp.30.637
+ ___block_descriptor_tmp.34.1089
+ ___block_descriptor_tmp.34.638
+ ___block_descriptor_tmp.36.1091
+ ___block_descriptor_tmp.37.1093
+ ___block_descriptor_tmp.4.1018
+ ___block_descriptor_tmp.4.1036
+ ___block_descriptor_tmp.4.908
+ ___block_descriptor_tmp.5.1034
+ ___block_descriptor_tmp.5.731
+ ___block_descriptor_tmp.5.911
+ ___block_descriptor_tmp.556
+ ___block_descriptor_tmp.565
+ ___block_descriptor_tmp.573
+ ___block_descriptor_tmp.6.1045
+ ___block_descriptor_tmp.6.734
+ ___block_descriptor_tmp.689
+ ___block_descriptor_tmp.7.1058
+ ___block_descriptor_tmp.7.726
+ ___block_descriptor_tmp.7.790
+ ___block_descriptor_tmp.756
+ ___block_descriptor_tmp.784
+ ___block_descriptor_tmp.8.1061
+ ___block_descriptor_tmp.8.737
+ ___block_descriptor_tmp.81.1119
+ ___block_descriptor_tmp.884
+ ___block_descriptor_tmp.9.1059
+ ___block_descriptor_tmp.9.791
+ ___block_descriptor_tmp.926
+ ___block_descriptor_tmp.947
+ ___block_descriptor_tmp.980
+ ___block_literal_global.1123
+ ___block_literal_global.554
+ ___block_literal_global.563
+ ___block_literal_global.571
+ ___block_literal_global.779
+ ___block_literal_global.909
- ___block_descriptor_tmp.1.1010
- ___block_descriptor_tmp.1.726
- ___block_descriptor_tmp.1.763
- ___block_descriptor_tmp.1.970
- ___block_descriptor_tmp.10.1063
- ___block_descriptor_tmp.10.904
- ___block_descriptor_tmp.1005
- ___block_descriptor_tmp.1033
- ___block_descriptor_tmp.11.1064
- ___block_descriptor_tmp.12.1065
- ___block_descriptor_tmp.12.897
- ___block_descriptor_tmp.13.1070
- ___block_descriptor_tmp.17.1074
- ___block_descriptor_tmp.17.960
- ___block_descriptor_tmp.2.730
- ___block_descriptor_tmp.2.768
- ___block_descriptor_tmp.2.896
- ___block_descriptor_tmp.2.974
- ___block_descriptor_tmp.26.1083
- ___block_descriptor_tmp.28.1086
- ___block_descriptor_tmp.3.732
- ___block_descriptor_tmp.3.769
- ___block_descriptor_tmp.3.789
- ___block_descriptor_tmp.3.906
- ___block_descriptor_tmp.30.638
- ___block_descriptor_tmp.34.1090
- ___block_descriptor_tmp.34.639
- ___block_descriptor_tmp.36.1092
- ___block_descriptor_tmp.37.1094
- ___block_descriptor_tmp.4.1019
- ___block_descriptor_tmp.4.1037
- ___block_descriptor_tmp.4.909
- ___block_descriptor_tmp.5.1035
- ___block_descriptor_tmp.5.733
- ___block_descriptor_tmp.5.912
- ___block_descriptor_tmp.557
- ___block_descriptor_tmp.566
- ___block_descriptor_tmp.574
- ___block_descriptor_tmp.6.1046
- ___block_descriptor_tmp.6.735
- ___block_descriptor_tmp.690
- ___block_descriptor_tmp.7.1059
- ___block_descriptor_tmp.7.728
- ___block_descriptor_tmp.7.791
- ___block_descriptor_tmp.757
- ___block_descriptor_tmp.785
- ___block_descriptor_tmp.8.1062
- ___block_descriptor_tmp.8.738
- ___block_descriptor_tmp.81.1120
- ___block_descriptor_tmp.885
- ___block_descriptor_tmp.9.1060
- ___block_descriptor_tmp.9.792
- ___block_descriptor_tmp.927
- ___block_descriptor_tmp.948
- ___block_descriptor_tmp.981
- ___block_literal_global.1124
- ___block_literal_global.555
- ___block_literal_global.564
- ___block_literal_global.572
- ___block_literal_global.780
- ___block_literal_global.910
Functions:
~ __container_traverse_parse_attrreference_buf : 660 -> 856
CStrings:
+ "@(#)VERSION:Container Manager: Feb 15 2026 08:00:30; MobileContainerManager_system-725.100.37~58/arm64e"
+ "Malformed attrlist on entry in [%s]; [%s][attr_dataoffset] field is negative; start = %p, end = 0x%lx, attr_dataoffset = %d, attr_length = %u"
- "@(#)VERSION:Container Manager: Jan 26 2026 08:15:06; MobileContainerManager_system-725.100.34~99/arm64e"

```
