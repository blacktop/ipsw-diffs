## WirelessRadioManagerd

> `/usr/sbin/WirelessRadioManagerd`

```diff

 1840.4.0.0.0
-  __TEXT.__text: 0x15dea4
+  __TEXT.__text: 0x15de98
   __TEXT.__auth_stubs: 0x24a0
   __TEXT.__objc_stubs: 0x1e040
   __TEXT.__init_offsets: 0x8

   __TEXT.__cstring: 0x4dbb3
   __TEXT.__objc_classname: 0x104e
   __TEXT.__objc_methname: 0x2ef21
-  __TEXT.__objc_methtype: 0x764a
+  __TEXT.__objc_methtype: 0x767a
   __TEXT.__dlopen_cstrs: 0x3ca
   __TEXT.__oslogstring: 0x90
   __TEXT.__unwind_info: 0x4698

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 14A1DB85-A251-31A0-9CFC-457FCE0F57C2
+  UUID: 3C20E38A-F42D-37AB-ADEE-A048D42E3364
   Functions: 6983
   Symbols:   814
   CStrings:  20859
Functions:
~ sub_10005ffb0 : 1128 -> 1096
~ sub_100075ba4 -> sub_100075b84 : 152 -> 160
~ sub_1000ad464 -> sub_1000ad44c : 296 -> 284
~ sub_1000adcb8 -> sub_1000adc94 : 296 -> 304
~ sub_1000b4470 -> sub_1000b4454 : 56 -> 60
~ sub_10015d22c -> sub_10015d214 : 108 -> 120
~ sub_10015d2cc -> sub_10015d2c0 : 160 -> 156
~ sub_10015d5a0 -> sub_10015d590 : 108 -> 120
~ sub_10015d648 -> sub_10015d644 : 108 -> 120
~ sub_10015d6dc -> sub_10015d6e4 : 260 -> 256
~ sub_10015db54 -> sub_10015db58 : 152 -> 148
~ sub_10015dcd4 : 124 -> 120
~ sub_10015ea80 -> sub_10015ea7c : 440 -> 436
~ sub_10015ec38 -> sub_10015ec30 : 436 -> 432
CStrings:
+ "{?=\"available\"B\"mcc\"I\"mnc\"I\"cellId\"Q\"lteCellInfoList\"{vector<(anonymous namespace)::WRM_LocationDbCellEntry, std::allocator<(anonymous namespace)::WRM_LocationDbCellEntry>>=\"__begin_\"^{WRM_LocationDbCellEntry}\"__end_\"^{WRM_LocationDbCellEntry}\"\"{?=\"__cap_\"^{WRM_LocationDbCellEntry}}}\"lteNsaCellInfoList\"{vector<(anonymous namespace)::WRM_LocationDbCellEntry, std::allocator<(anonymous namespace)::WRM_LocationDbCellEntry>>=\"__begin_\"^{WRM_LocationDbCellEntry}\"__end_\"^{WRM_LocationDbCellEntry}\"\"{?=\"__cap_\"^{WRM_LocationDbCellEntry}}}\"saCellInfoList\"{vector<(anonymous namespace)::WRM_LocationDbCellEntry, std::allocator<(anonymous namespace)::WRM_LocationDbCellEntry>>=\"__begin_\"^{WRM_LocationDbCellEntry}\"__end_\"^{WRM_LocationDbCellEntry}\"\"{?=\"__cap_\"^{WRM_LocationDbCellEntry}}}\"sadcCellInfoList\"{vector<(anonymous namespace)::WRM_LocationDbCellEntry, std::allocator<(anonymous namespace)::WRM_LocationDbCellEntry>>=\"__begin_\"^{WRM_LocationDbCellEntry}\"__end_\"^{WRM_LocationDbCellEntry}\"\"{?=\"__cap_\"^{WRM_LocationDbCellEntry}}}}"
+ "{?=\"available\"B\"mcc\"I\"mnc\"I\"cellId\"Q\"lteCellInfoList\"{vector<IBICallPsWrmSdmLocationDBCellPerRatInfo, std::allocator<IBICallPsWrmSdmLocationDBCellPerRatInfo>>=\"__begin_\"^{IBICallPsWrmSdmLocationDBCellPerRatInfo}\"__end_\"^{IBICallPsWrmSdmLocationDBCellPerRatInfo}\"\"{?=\"__cap_\"^{IBICallPsWrmSdmLocationDBCellPerRatInfo}}}\"lteNsaCellInfoList\"{vector<IBICallPsWrmSdmLocationDBCellPerRatInfo, std::allocator<IBICallPsWrmSdmLocationDBCellPerRatInfo>>=\"__begin_\"^{IBICallPsWrmSdmLocationDBCellPerRatInfo}\"__end_\"^{IBICallPsWrmSdmLocationDBCellPerRatInfo}\"\"{?=\"__cap_\"^{IBICallPsWrmSdmLocationDBCellPerRatInfo}}}\"saCellInfoList\"{vector<IBICallPsWrmSdmLocationDBCellPerRatInfo, std::allocator<IBICallPsWrmSdmLocationDBCellPerRatInfo>>=\"__begin_\"^{IBICallPsWrmSdmLocationDBCellPerRatInfo}\"__end_\"^{IBICallPsWrmSdmLocationDBCellPerRatInfo}\"\"{?=\"__cap_\"^{IBICallPsWrmSdmLocationDBCellPerRatInfo}}}\"sadcCellInfoList\"{vector<IBICallPsWrmSdmLocationDBCellPerRatInfo, std::allocator<IBICallPsWrmSdmLocationDBCellPerRatInfo>>=\"__begin_\"^{IBICallPsWrmSdmLocationDBCellPerRatInfo}\"__end_\"^{IBICallPsWrmSdmLocationDBCellPerRatInfo}\"\"{?=\"__cap_\"^{IBICallPsWrmSdmLocationDBCellPerRatInfo}}}}"
- "{?=\"available\"B\"mcc\"I\"mnc\"I\"cellId\"Q\"lteCellInfoList\"{vector<(anonymous namespace)::WRM_LocationDbCellEntry, std::allocator<(anonymous namespace)::WRM_LocationDbCellEntry>>=\"__begin_\"^{WRM_LocationDbCellEntry}\"__end_\"^{WRM_LocationDbCellEntry}\"__cap_\"^{WRM_LocationDbCellEntry}}\"lteNsaCellInfoList\"{vector<(anonymous namespace)::WRM_LocationDbCellEntry, std::allocator<(anonymous namespace)::WRM_LocationDbCellEntry>>=\"__begin_\"^{WRM_LocationDbCellEntry}\"__end_\"^{WRM_LocationDbCellEntry}\"__cap_\"^{WRM_LocationDbCellEntry}}\"saCellInfoList\"{vector<(anonymous namespace)::WRM_LocationDbCellEntry, std::allocator<(anonymous namespace)::WRM_LocationDbCellEntry>>=\"__begin_\"^{WRM_LocationDbCellEntry}\"__end_\"^{WRM_LocationDbCellEntry}\"__cap_\"^{WRM_LocationDbCellEntry}}\"sadcCellInfoList\"{vector<(anonymous namespace)::WRM_LocationDbCellEntry, std::allocator<(anonymous namespace)::WRM_LocationDbCellEntry>>=\"__begin_\"^{WRM_LocationDbCellEntry}\"__end_\"^{WRM_LocationDbCellEntry}\"__cap_\"^{WRM_LocationDbCellEntry}}}"
- "{?=\"available\"B\"mcc\"I\"mnc\"I\"cellId\"Q\"lteCellInfoList\"{vector<IBICallPsWrmSdmLocationDBCellPerRatInfo, std::allocator<IBICallPsWrmSdmLocationDBCellPerRatInfo>>=\"__begin_\"^{IBICallPsWrmSdmLocationDBCellPerRatInfo}\"__end_\"^{IBICallPsWrmSdmLocationDBCellPerRatInfo}\"__cap_\"^{IBICallPsWrmSdmLocationDBCellPerRatInfo}}\"lteNsaCellInfoList\"{vector<IBICallPsWrmSdmLocationDBCellPerRatInfo, std::allocator<IBICallPsWrmSdmLocationDBCellPerRatInfo>>=\"__begin_\"^{IBICallPsWrmSdmLocationDBCellPerRatInfo}\"__end_\"^{IBICallPsWrmSdmLocationDBCellPerRatInfo}\"__cap_\"^{IBICallPsWrmSdmLocationDBCellPerRatInfo}}\"saCellInfoList\"{vector<IBICallPsWrmSdmLocationDBCellPerRatInfo, std::allocator<IBICallPsWrmSdmLocationDBCellPerRatInfo>>=\"__begin_\"^{IBICallPsWrmSdmLocationDBCellPerRatInfo}\"__end_\"^{IBICallPsWrmSdmLocationDBCellPerRatInfo}\"__cap_\"^{IBICallPsWrmSdmLocationDBCellPerRatInfo}}\"sadcCellInfoList\"{vector<IBICallPsWrmSdmLocationDBCellPerRatInfo, std::allocator<IBICallPsWrmSdmLocationDBCellPerRatInfo>>=\"__begin_\"^{IBICallPsWrmSdmLocationDBCellPerRatInfo}\"__end_\"^{IBICallPsWrmSdmLocationDBCellPerRatInfo}\"__cap_\"^{IBICallPsWrmSdmLocationDBCellPerRatInfo}}}"

```
