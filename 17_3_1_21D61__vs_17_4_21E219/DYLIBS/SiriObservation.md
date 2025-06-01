## SiriObservation

> `/System/Library/PrivateFrameworks/SiriObservation.framework/SiriObservation`

```diff

-3303.9.1.0.0
+3304.85.3.0.0
   __TEXT.__text: 0x15bd8
   __TEXT.__auth_stubs: 0x570
   __TEXT.__objc_methlist: 0xf74

   __TEXT.__oslogstring: 0x6d4
   __TEXT.__unwind_info: 0x714
   __TEXT.__objc_classname: 0x270
-  __TEXT.__objc_methname: 0x1fad
+  __TEXT.__objc_methname: 0x1fc1
   __TEXT.__objc_methtype: 0x999
   __TEXT.__objc_stubs: 0x1dc0
   __DATA_CONST.__got: 0x50

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x1fd8
   __DATA_CONST.__objc_selrefs: 0x898
+  __DATA_CONST.__objc_classrefs: 0x138
+  __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0xc0
   __AUTH_CONST.__const: 0x620
   __AUTH_CONST.__cfstring: 0xa20

   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__auth_got: 0x2c8
   __AUTH.__objc_data: 0x230
-  __AUTH.__data: 0x40
-  __DATA.__objc_classrefs: 0x138
-  __DATA.__objc_superrefs: 0x80
+  __AUTH.__data: 0x80
   __DATA.__objc_ivar: 0x1bc
   __DATA.__data: 0x420
-  __DATA.__bss: 0xd0
+  __DATA.__bss: 0x160
   __DATA_DIRTY.__objc_data: 0x2d0
-  __DATA_DIRTY.__data: 0xf8
-  __DATA_DIRTY.__bss: 0x240
+  __DATA_DIRTY.__data: 0xb8
+  __DATA_DIRTY.__bss: 0x1b0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8E419CCC-AEE2-39A3-B00A-908FA6C8503C
+  UUID: 79DD1CE8-1AF1-38B1-9644-2E6FC23B4971
   Functions: 598
   Symbols:   2108
-  CStrings:  892
+  CStrings:  893
 
Symbols:
+ _MTAlarmManagerAlarmFiredFunction.173
+ _MTAlarmManagerAlarmsAddedFunction.200
+ _MTAlarmManagerAlarmsRemovedFunction.181
+ _MTAlarmManagerAlarmsUpdatedFunction.189
+ _MTAlarmManagerFiringAlarmChangedFunction.165
+ _MTAlarmManagerFiringAlarmDismissedFunction.157
+ _MTAlarmManagerFunction.220
+ _MTAlarmManagerStateResetFunction.145
+ _MTTimerManagerFiringTimerChangedFunction.1054
+ _MTTimerManagerFiringTimerDismissedFunction.1045
+ _MTTimerManagerFunction.1113
+ _MTTimerManagerStateResetFunction.1032
+ _MTTimerManagerTimerFiredFunction.1063
+ _MTTimerManagerTimersAddedFunction.1089
+ _MTTimerManagerTimersRemovedFunction.1071
+ _MTTimerManagerTimersUpdatedFunction.1079
+ _MobileTimerLibrary.sLib.1029
+ _MobileTimerLibrary.sLib.143
+ _MobileTimerLibrary.sLib.948
+ _MobileTimerLibrary.sOnce.1028
+ _MobileTimerLibrary.sOnce.141
+ _MobileTimerLibrary.sOnce.947
+ ___MobileTimerLibrary_block_invoke.1034
+ ___MobileTimerLibrary_block_invoke.148
+ ___MobileTimerLibrary_block_invoke.951
+ ___block_literal_global.1106
+ ___block_literal_global.1141
+ ___block_literal_global.214
+ ___block_literal_global.309
+ ___block_literal_global.62.142
+ ___block_literal_global.62.968
+ ___block_literal_global.641
+ ___block_literal_global.65.193
+ ___block_literal_global.65.965
+ ___block_literal_global.68.962
+ ___block_literal_global.71.959
+ ___block_literal_global.74.956
+ ___block_literal_global.77.953
+ ___block_literal_global.80.945
+ ___block_literal_global.83.137
+ ___block_literal_global.979
+ ___initMTAlarmManagerAlarmFired_block_invoke.171
+ ___initMTAlarmManagerAlarmsAdded_block_invoke.197
+ ___initMTAlarmManagerAlarmsRemoved_block_invoke.179
+ ___initMTAlarmManagerAlarmsUpdated_block_invoke.187
+ ___initMTAlarmManagerFiringAlarmChanged_block_invoke.163
+ ___initMTAlarmManagerFiringAlarmDismissed_block_invoke.155
+ ___initMTAlarmManagerStateReset_block_invoke.140
+ ___initMTAlarmManager_block_invoke.218
+ ___initMTTimerManagerFiringTimerChanged_block_invoke.1051
+ ___initMTTimerManagerFiringTimerDismissed_block_invoke.1042
+ ___initMTTimerManagerStateReset_block_invoke.1027
+ ___initMTTimerManagerTimerFired_block_invoke.1060
+ ___initMTTimerManagerTimersAdded_block_invoke.1086
+ ___initMTTimerManagerTimersRemoved_block_invoke.1069
+ ___initMTTimerManagerTimersUpdated_block_invoke.1077
+ ___initMTTimerManager_block_invoke.1110
+ __unnamed_array_storage.645
+ _classMTAlarmManager.215
+ _classMTTimerManager.1107
+ _constantMTAlarmManagerAlarmFired.169
+ _constantMTAlarmManagerAlarmsAdded.194
+ _constantMTAlarmManagerAlarmsRemoved.177
+ _constantMTAlarmManagerAlarmsUpdated.185
+ _constantMTAlarmManagerFiringAlarmChanged.161
+ _constantMTAlarmManagerFiringAlarmDismissed.153
+ _constantMTAlarmManagerStateReset.138
+ _constantMTTimerManagerFiringTimerChanged.1049
+ _constantMTTimerManagerFiringTimerDismissed.1040
+ _constantMTTimerManagerStateReset.1025
+ _constantMTTimerManagerTimerFired.1058
+ _constantMTTimerManagerTimersAdded.1083
+ _constantMTTimerManagerTimersRemoved.1067
+ _constantMTTimerManagerTimersUpdated.1075
+ _getMTAlarmManagerAlarmFired.130
+ _getMTAlarmManagerAlarmsAdded.127
+ _getMTAlarmManagerAlarmsRemoved.129
+ _getMTAlarmManagerAlarmsUpdated.128
+ _getMTAlarmManagerClass.207
+ _getMTAlarmManagerFiringAlarmChanged.131
+ _getMTAlarmManagerFiringAlarmDismissed.132
+ _getMTAlarmManagerStateReset.133
+ _getMTTimerManagerClass.1100
+ _getMTTimerManagerFiringTimerChanged.1019
+ _getMTTimerManagerFiringTimerDismissed.1020
+ _getMTTimerManagerStateReset.1021
+ _getMTTimerManagerTimerFired.1018
+ _getMTTimerManagerTimersAdded.1015
+ _getMTTimerManagerTimersRemoved.1017
+ _getMTTimerManagerTimersUpdated.1016
+ _initMTAlarmManager.212
+ _initMTAlarmManager.sOnce.213
+ _initMTAlarmManagerAlarmFired.167
+ _initMTAlarmManagerAlarmFired.sOnce.168
+ _initMTAlarmManagerAlarmsAdded.191
+ _initMTAlarmManagerAlarmsAdded.sOnce.192
+ _initMTAlarmManagerAlarmsRemoved.175
+ _initMTAlarmManagerAlarmsRemoved.sOnce.176
+ _initMTAlarmManagerAlarmsUpdated.183
+ _initMTAlarmManagerAlarmsUpdated.sOnce.184
+ _initMTAlarmManagerFiringAlarmChanged.159
+ _initMTAlarmManagerFiringAlarmChanged.sOnce.160
+ _initMTAlarmManagerFiringAlarmDismissed.151
+ _initMTAlarmManagerFiringAlarmDismissed.sOnce.152
+ _initMTAlarmManagerStateReset.135
+ _initMTAlarmManagerStateReset.sOnce.136
+ _initMTTimerManager.1104
+ _initMTTimerManager.sOnce.1105
+ _initMTTimerManagerFiringTimerChanged.1047
+ _initMTTimerManagerFiringTimerChanged.sOnce.1048
+ _initMTTimerManagerFiringTimerDismissed.1038
+ _initMTTimerManagerFiringTimerDismissed.sOnce.1039
+ _initMTTimerManagerStateReset.1023
+ _initMTTimerManagerStateReset.sOnce.1024
+ _initMTTimerManagerTimerFired.1056
+ _initMTTimerManagerTimerFired.sOnce.1057
+ _initMTTimerManagerTimersAdded.1081
+ _initMTTimerManagerTimersAdded.sOnce.1082
+ _initMTTimerManagerTimersRemoved.1065
+ _initMTTimerManagerTimersRemoved.sOnce.1066
+ _initMTTimerManagerTimersUpdated.1073
+ _initMTTimerManagerTimersUpdated.sOnce.1074
- _MTAlarmManagerAlarmFiredFunction.172
- _MTAlarmManagerAlarmsAddedFunction.199
- _MTAlarmManagerAlarmsRemovedFunction.180
- _MTAlarmManagerAlarmsUpdatedFunction.188
- _MTAlarmManagerFiringAlarmChangedFunction.164
- _MTAlarmManagerFiringAlarmDismissedFunction.156
- _MTAlarmManagerFunction.219
- _MTAlarmManagerStateResetFunction.144
- _MTTimerManagerFiringTimerChangedFunction.1041
- _MTTimerManagerFiringTimerDismissedFunction.1032
- _MTTimerManagerFunction.1100
- _MTTimerManagerStateResetFunction.1019
- _MTTimerManagerTimerFiredFunction.1050
- _MTTimerManagerTimersAddedFunction.1076
- _MTTimerManagerTimersRemovedFunction.1058
- _MTTimerManagerTimersUpdatedFunction.1066
- _MobileTimerLibrary.sLib.1016
- _MobileTimerLibrary.sLib.142
- _MobileTimerLibrary.sLib.935
- _MobileTimerLibrary.sOnce.1015
- _MobileTimerLibrary.sOnce.140
- _MobileTimerLibrary.sOnce.934
- ___MobileTimerLibrary_block_invoke.1021
- ___MobileTimerLibrary_block_invoke.147
- ___MobileTimerLibrary_block_invoke.938
- ___block_literal_global.1093
- ___block_literal_global.1128
- ___block_literal_global.213
- ___block_literal_global.307
- ___block_literal_global.62.141
- ___block_literal_global.62.955
- ___block_literal_global.639
- ___block_literal_global.65.192
- ___block_literal_global.65.952
- ___block_literal_global.68.949
- ___block_literal_global.71.946
- ___block_literal_global.74.943
- ___block_literal_global.77.940
- ___block_literal_global.80.932
- ___block_literal_global.83.136
- ___block_literal_global.966
- ___initMTAlarmManagerAlarmFired_block_invoke.170
- ___initMTAlarmManagerAlarmsAdded_block_invoke.196
- ___initMTAlarmManagerAlarmsRemoved_block_invoke.178
- ___initMTAlarmManagerAlarmsUpdated_block_invoke.186
- ___initMTAlarmManagerFiringAlarmChanged_block_invoke.162
- ___initMTAlarmManagerFiringAlarmDismissed_block_invoke.154
- ___initMTAlarmManagerStateReset_block_invoke.139
- ___initMTAlarmManager_block_invoke.217
- ___initMTTimerManagerFiringTimerChanged_block_invoke.1038
- ___initMTTimerManagerFiringTimerDismissed_block_invoke.1029
- ___initMTTimerManagerStateReset_block_invoke.1014
- ___initMTTimerManagerTimerFired_block_invoke.1047
- ___initMTTimerManagerTimersAdded_block_invoke.1073
- ___initMTTimerManagerTimersRemoved_block_invoke.1056
- ___initMTTimerManagerTimersUpdated_block_invoke.1064
- ___initMTTimerManager_block_invoke.1097
- __unnamed_array_storage.643
- _classMTAlarmManager.214
- _classMTTimerManager.1094
- _constantMTAlarmManagerAlarmFired.168
- _constantMTAlarmManagerAlarmsAdded.193
- _constantMTAlarmManagerAlarmsRemoved.176
- _constantMTAlarmManagerAlarmsUpdated.184
- _constantMTAlarmManagerFiringAlarmChanged.160
- _constantMTAlarmManagerFiringAlarmDismissed.152
- _constantMTAlarmManagerStateReset.137
- _constantMTTimerManagerFiringTimerChanged.1036
- _constantMTTimerManagerFiringTimerDismissed.1027
- _constantMTTimerManagerStateReset.1012
- _constantMTTimerManagerTimerFired.1045
- _constantMTTimerManagerTimersAdded.1070
- _constantMTTimerManagerTimersRemoved.1054
- _constantMTTimerManagerTimersUpdated.1062
- _getMTAlarmManagerAlarmFired.129
- _getMTAlarmManagerAlarmsAdded.126
- _getMTAlarmManagerAlarmsRemoved.128
- _getMTAlarmManagerAlarmsUpdated.127
- _getMTAlarmManagerClass.206
- _getMTAlarmManagerFiringAlarmChanged.130
- _getMTAlarmManagerFiringAlarmDismissed.131
- _getMTAlarmManagerStateReset.132
- _getMTTimerManagerClass.1087
- _getMTTimerManagerFiringTimerChanged.1006
- _getMTTimerManagerFiringTimerDismissed.1007
- _getMTTimerManagerStateReset.1008
- _getMTTimerManagerTimerFired.1005
- _getMTTimerManagerTimersAdded.1002
- _getMTTimerManagerTimersRemoved.1004
- _getMTTimerManagerTimersUpdated.1003
- _initMTAlarmManager.211
- _initMTAlarmManager.sOnce.212
- _initMTAlarmManagerAlarmFired.166
- _initMTAlarmManagerAlarmFired.sOnce.167
- _initMTAlarmManagerAlarmsAdded.190
- _initMTAlarmManagerAlarmsAdded.sOnce.191
- _initMTAlarmManagerAlarmsRemoved.174
- _initMTAlarmManagerAlarmsRemoved.sOnce.175
- _initMTAlarmManagerAlarmsUpdated.182
- _initMTAlarmManagerAlarmsUpdated.sOnce.183
- _initMTAlarmManagerFiringAlarmChanged.158
- _initMTAlarmManagerFiringAlarmChanged.sOnce.159
- _initMTAlarmManagerFiringAlarmDismissed.150
- _initMTAlarmManagerFiringAlarmDismissed.sOnce.151
- _initMTAlarmManagerStateReset.134
- _initMTAlarmManagerStateReset.sOnce.135
- _initMTTimerManager.1091
- _initMTTimerManager.sOnce.1092
- _initMTTimerManagerFiringTimerChanged.1034
- _initMTTimerManagerFiringTimerChanged.sOnce.1035
- _initMTTimerManagerFiringTimerDismissed.1025
- _initMTTimerManagerFiringTimerDismissed.sOnce.1026
- _initMTTimerManagerStateReset.1010
- _initMTTimerManagerStateReset.sOnce.1011
- _initMTTimerManagerTimerFired.1043
- _initMTTimerManagerTimerFired.sOnce.1044
- _initMTTimerManagerTimersAdded.1068
- _initMTTimerManagerTimersAdded.sOnce.1069
- _initMTTimerManagerTimersRemoved.1052
- _initMTTimerManagerTimersRemoved.sOnce.1053
- _initMTTimerManagerTimersUpdated.1060
- _initMTTimerManagerTimersUpdated.sOnce.1061
CStrings:
+ "T@\"NSString\",?,R,C"

```
