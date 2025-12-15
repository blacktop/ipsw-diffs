## CoreWiFi

> `/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`

```diff

-988.12.4.5.0
-  __TEXT.__text: 0x1b0ee4
+991.1.0.0.0
+  __TEXT.__text: 0x1b17a4
   __TEXT.__auth_stubs: 0x1ad0
   __TEXT.__objc_methlist: 0x1081c
   __TEXT.__const: 0x2f18

   __TEXT.__swift5_fieldmd: 0x6a0
   __TEXT.__swift5_proto: 0x270
   __TEXT.__swift5_types: 0xac
-  __TEXT.__cstring: 0x1e13f
+  __TEXT.__cstring: 0x206a3
   __TEXT.__gcc_except_tab: 0x7b9c
-  __TEXT.__oslogstring: 0x1ba5c
+  __TEXT.__oslogstring: 0x1be8d
   __TEXT.__ustring: 0x4
   __TEXT.__unwind_info: 0x5588
   __TEXT.__eh_frame: 0x570
   __TEXT.__objc_classname: 0xfb1
-  __TEXT.__objc_methname: 0x27a0e
-  __TEXT.__objc_methtype: 0x3934
-  __TEXT.__objc_stubs: 0x1c4c0
+  __TEXT.__objc_methname: 0x27a14
+  __TEXT.__objc_methtype: 0x3927
+  __TEXT.__objc_stubs: 0x1c440
   __DATA_CONST.__got: 0x918
-  __DATA_CONST.__const: 0x50b0
+  __DATA_CONST.__const: 0x50d8
   __DATA_CONST.__objc_classlist: 0x3a8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8340
+  __DATA_CONST.__objc_selrefs: 0x8330
   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x338
-  __DATA_CONST.__objc_arraydata: 0x1a00
+  __DATA_CONST.__objc_arraydata: 0x1eb0
   __AUTH_CONST.__auth_got: 0xd78
   __AUTH_CONST.__const: 0x32d0
-  __AUTH_CONST.__cfstring: 0x18340
-  __AUTH_CONST.__objc_const: 0x15918
+  __AUTH_CONST.__cfstring: 0x19740
+  __AUTH_CONST.__objc_const: 0x158e8
   __AUTH_CONST.__objc_arrayobj: 0x450
   __AUTH_CONST.__objc_intobj: 0x3828
   __AUTH_CONST.__objc_dictobj: 0x230
   __AUTH.__objc_data: 0xe58
   __AUTH.__data: 0x320
-  __DATA.__objc_ivar: 0x1260
+  __DATA.__objc_ivar: 0x125c
   __DATA.__data: 0x1700
   __DATA.__bss: 0x4fa0
   __DATA.__common: 0x10

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 14745B05-6B6F-3097-BE1E-C2EBCDB4B16A
-  Functions: 7548
+  UUID: 078AE96C-9A0C-31BF-A498-EE765A58BA04
+  Functions: 7549
   Symbols:   1082
-  CStrings:  15095
+  CStrings:  15424
 
CStrings:
+ "-[CWFAutoJoinMetric coreAnalyticsEventPayload]"
+ "-[CWFNetworkProfile setPayloadIdentifier:]"
+ "-[CWFWiFiNetworkSharingManager __checkTCCAuthorizationStatus]"
+ "-[CWFWiFiNetworkSharingManager __deviceForClientID:]"
+ "Ti,V_deviceAccessAuthorizationNotifyToken"
+ "[corewifi] %s: coreAnalyticsEventPayload CARRIER_PAYLOAD_IDENTIFIER NOT ALLOWED"
+ "[corewifi] %s: coreAnalyticsEventPayload CARRIER_PAYLOAD_IDENTIFIER OK approved %d payloadIdentifier %@"
+ "[corewifi] %s: coreAnalyticsEventPayload addReason is not CarrierBundle"
+ "[corewifi] %s: coreAnalyticsEventPayload payloadIdentifier is nil but addReason is CarrierBundle"
+ "[corewifi] %s: setPayloadIdentifier %@ networkName %@ approved %@ waspayloadIdentifier %@ cb %d _internal %@"
+ "[corewifi] %s: setPayloadIdentifier done %@ networkName %@ approved %@ payloadIdentifier %@ cb %d _internal %@"
+ "[corewifi] %{public}s (%{public}s:%u) [wifi-network-sharing] [DASession getDevicesWithFlags:session:error:] failed (error=%{public}@)"
+ "[corewifi] [wifi-network-sharing] Could not send network list update, no matching clients are registered for the event (clientID=%{public}@)"
+ "[corewifi] [wifi-network-sharing] Invalidated XPC connection (conn=%{public}@)"
+ "[corewifi] [wifi-network-sharing] Received device access authorization update"
+ "[corewifi] [wifi-network-sharing] Started monitoring device access authorization updates"
+ "[corewifi] [wifi-network-sharing] Stopped monitoring device access authorization updates"
+ "[corewifi] [wifi-network-sharing] [DASession getAuthorizedDevices:] completed (device=%{public}@, clientID=%{public}@, error=%{public}@)"
+ "__checkTCCAuthorizationStatus"
+ "__startMonitoringDeviceAccessAuthorization"
+ "__stopMonitoringDeviceAccessAuthorization"
+ "_deviceAccessAuthorizationNotifyToken"
+ "carrierPayloadIdentifier(telemetryApproved=%d)=%@, "
+ "com.apple.8ta_za.4a790998-d474-11eb-9b3f-f45c89abb0d9"
+ "com.apple.AIS_th.465bff14-d474-11eb-a080-f45c89abb0d9"
+ "com.apple.ATT_FirstNet_US.5a7a5e14-d474-11eb-b015-f45c89abb0d9"
+ "com.apple.ATT_FirstNet_US.5a7a5f86-d474-11eb-b015-f45c89abb0d9"
+ "com.apple.ATT_FirstNet_US.5a7a5ff4-d474-11eb-b015-f45c89abb0d9"
+ "com.apple.ATT_NR_US.5f790ec4-d474-11eb-b1a8-f45c89abb0d9"
+ "com.apple.ATT_NR_US.5f791004-d474-11eb-b1a8-f45c89abb0d9"
+ "com.apple.ATT_NR_US.5f79105e-d474-11eb-b1a8-f45c89abb0d9"
+ "com.apple.ATT_US.44f80276-d474-11eb-ab3a-f45c89abb0d9"
+ "com.apple.ATT_US.599e00a4-d474-11eb-9b5b-f45c89abb0d9"
+ "com.apple.ATT_US.599e0202-d474-11eb-9b5b-f45c89abb0d9"
+ "com.apple.ATT_US.599e0270-d474-11eb-9b5b-f45c89abb0d9"
+ "com.apple.Batelco_bh.43a98ea8-d474-11eb-a640-f45c89abb0d9"
+ "com.apple.Bell_ca.49b3016c-d474-11eb-ab35-f45c89abb0d9"
+ "com.apple.Bell_ca.49b302d4-d474-11eb-ab35-f45c89abb0d9"
+ "com.apple.Bell_ca.60375974-d474-11eb-ac08-f45c89abb0d9"
+ "com.apple.Bell_ca.60375ac8-d474-11eb-ac08-f45c89abb0d9"
+ "com.apple.CSL_hk.48ef1aea-d474-11eb-b10a-f45c89abb0d9"
+ "com.apple.CSL_hk.48ef1c02-d474-11eb-b10a-f45c89abb0d9"
+ "com.apple.Chunghwa_tw.4743286c-d474-11eb-9077-f45c89abb0d9"
+ "com.apple.Chunghwa_tw.5cc716c6-d474-11eb-af60-f45c89abb0d9"
+ "com.apple.Cyta_cy.E51BB02F-FC15-42B7-82CE-AFCF12BAF106"
+ "com.apple.DeviceAccess.authorizationUpdated"
+ "com.apple.Docomo_gu.5a9cfeb0-d474-11eb-9636-f45c89abb0d9"
+ "com.apple.Docomo_jp.5fe68616-d474-11eb-8141-f45c89abb0d9"
+ "com.apple.FreedomMobile_ca.451889f6-d474-11eb-84cc-f45c89abb0d9"
+ "com.apple.Hutchison_HKBN_hk.60a184ca-d474-11eb-b9f4-f45c89abb0d9"
+ "com.apple.Hutchison_hk.461b2d0e-d474-11eb-8834-f45c89abb0d9"
+ "com.apple.Hutchison_hk.5b08aaf2-d474-11eb-bb7c-f45c89abb0d9"
+ "com.apple.KDDI_LTE_only_jp.47008bc4-d474-11eb-8412-f45c89abb0d9"
+ "com.apple.KDDI_LTE_only_jp.5c7ea86e-d474-11eb-9771-f45c89abb0d9"
+ "com.apple.KTF_kr.46be6dd4-d474-11eb-86cf-f45c89abb0d9"
+ "com.apple.KTF_kr.46be6fb4-d474-11eb-86cf-f45c89abb0d9"
+ "com.apple.KTF_kr.46be7018-d474-11eb-86cf-f45c89abb0d9"
+ "com.apple.KTF_kr.46be705e-d474-11eb-86cf-f45c89abb0d9"
+ "com.apple.KTF_kr.5c0a10ee-d474-11eb-b7b7-f45c89abb0d9"
+ "com.apple.KTF_kr.5c0a12ce-d474-11eb-b7b7-f45c89abb0d9"
+ "com.apple.KTF_kr.5c0a1382-d474-11eb-b7b7-f45c89abb0d9"
+ "com.apple.KTF_kr.5c0a13dc-d474-11eb-b7b7-f45c89abb0d9"
+ "com.apple.LGU_kr.47e4fac8-d474-11eb-90a1-f45c89abb0d9"
+ "com.apple.LGU_kr.47e4fba6-d474-11eb-90a1-f45c89abb0d9"
+ "com.apple.LGU_kr.47e4fcdc-d474-11eb-90a1-f45c89abb0d9"
+ "com.apple.LGU_kr.47e4fd4a-d474-11eb-90a1-f45c89abb0d9"
+ "com.apple.LGU_kr.47e4fd90-d474-11eb-90a1-f45c89abb0d9"
+ "com.apple.LGU_kr.5dc65ac8-d474-11eb-ac3d-f45c89abb0d9"
+ "com.apple.LGU_kr.5dc65c8a-d474-11eb-ac3d-f45c89abb0d9"
+ "com.apple.LGU_kr.5dc65dfc-d474-11eb-ac3d-f45c89abb0d9"
+ "com.apple.LGU_kr.5dc65e6a-d474-11eb-ac3d-f45c89abb0d9"
+ "com.apple.LGU_kr.5dc65eba-d474-11eb-ac3d-f45c89abb0d9"
+ "com.apple.MTS_ca.5b2a648a-d474-11eb-aa99-f45c89abb0d9"
+ "com.apple.Maxis_my.5be45444-d474-11eb-a21c-f45c89abb0d9"
+ "com.apple.Mirs_il.494fe5c8-d474-11eb-aff9-f45c89abb0d9"
+ "com.apple.Mirs_il.5f9dbfa8-d474-11eb-9459-f45c89abb0d9"
+ "com.apple.MobiCom_mn.AC0BD320-4350-4230-87F8-3A6E0CBE6265"
+ "com.apple.MobileOne_sg.4492ff20-d474-11eb-bf2a-f45c89abb0d9"
+ "com.apple.MobileOne_sg.58bc4498-d474-11eb-8bc5-f45c89abb0d9"
+ "com.apple.O2_Prepaid_UK.59512e0a-d474-11eb-a044-f45c89abb0d9"
+ "com.apple.O2_Prepaid_UK.59512fa4-d474-11eb-a044-f45c89abb0d9"
+ "com.apple.O2_Prepaid_UK.5951306c-d474-11eb-a044-f45c89abb0d9"
+ "com.apple.O2_UK.4471d28c-d474-11eb-adde-f45c89abb0d9"
+ "com.apple.O2_UK.4471d4c6-d474-11eb-adde-f45c89abb0d9"
+ "com.apple.O2_UK.4471d516-d474-11eb-adde-f45c89abb0d9"
+ "com.apple.O2_UK.5899e0b0-d474-11eb-a9ed-f45c89abb0d9"
+ "com.apple.O2_UK.5899e254-d474-11eb-a9ed-f45c89abb0d9"
+ "com.apple.O2_UK.5899e2ea-d474-11eb-a9ed-f45c89abb0d9"
+ "com.apple.Omnitel_lt.43ca4b66-d474-11eb-91a4-f45c89abb0d9"
+ "com.apple.Orange_pl.4762ba56-d474-11eb-bf95-f45c89abb0d9"
+ "com.apple.Orange_pl.5ceb0a5e-d474-11eb-a924-f45c89abb0d9"
+ "com.apple.Orange_ro.4538b6c2-d474-11eb-907d-f45c89abb0d9"
+ "com.apple.Orange_ro.4538b7f8-d474-11eb-907d-f45c89abb0d9"
+ "com.apple.Orange_ro.59c08084-d474-11eb-b64d-f45c89abb0d9"
+ "com.apple.Orange_ro.59c082c8-d474-11eb-b64d-f45c89abb0d9"
+ "com.apple.Orange_uk.5f5660e0-d474-11eb-91b3-f45c89abb0d9"
+ "com.apple.PCCW_hk.4845f0b4-d474-11eb-85d2-f45c89abb0d9"
+ "com.apple.PCCW_hk.4845f1f4-d474-11eb-85d2-f45c89abb0d9"
+ "com.apple.RelianceJio_in.4805368c-d474-11eb-93ee-f45c89abb0d9"
+ "com.apple.RelianceJio_in.5dec012e-d474-11eb-a0f5-f45c89abb0d9"
+ "com.apple.SFR_re.59e238f0-d474-11eb-9ec5-f45c89abb0d9"
+ "com.apple.STC_sa.4558d01a-d474-11eb-8552-f45c89abb0d9"
+ "com.apple.STC_sa.4558d150-d474-11eb-8552-f45c89abb0d9"
+ "com.apple.STC_sa.5a075cde-d474-11eb-810b-f45c89abb0d9"
+ "com.apple.STC_sa.5a075e46-d474-11eb-810b-f45c89abb0d9"
+ "com.apple.Sasktel_ca.47c31e50-d474-11eb-95a7-f45c89abb0d9"
+ "com.apple.Sasktel_ca.5d55a882-d474-11eb-8912-f45c89abb0d9"
+ "com.apple.Shinetown.582ef5d4-d474-11eb-ba3a-f45c89abb0d9"
+ "com.apple.SingTel_sg.47a2b124-d474-11eb-9a67-f45c89abb0d9"
+ "com.apple.SingTel_sg.47a2b246-d474-11eb-9a67-f45c89abb0d9"
+ "com.apple.SingTel_sg.5d33b9a2-d474-11eb-8f88-f45c89abb0d9"
+ "com.apple.SingTel_sg.5d33bb0a-d474-11eb-8f88-f45c89abb0d9"
+ "com.apple.Softbank_jp.5da01106-d474-11eb-a708-f45c89abb0d9"
+ "com.apple.Sprint_ISIM_LTE_US.45bc0eaa-d474-11eb-9a79-f45c89abb0d9"
+ "com.apple.Sprint_ISIM_LTE_US.5ac08826-d474-11eb-8b3e-f45c89abb0d9"
+ "com.apple.Swisscom_ch.4721a4da-d474-11eb-a8c1-f45c89abb0d9"
+ "com.apple.Swisscom_ch.5ca257fa-d474-11eb-8298-f45c89abb0d9"
+ "com.apple.Swisscom_ch.5ca25980-d474-11eb-8298-f45c89abb0d9"
+ "com.apple.Swisscom_ch.5ca259e4-d474-11eb-8298-f45c89abb0d9"
+ "com.apple.TMobile_Germany.488c866e-d474-11eb-8b0f-f45c89abb0d9"
+ "com.apple.TMobile_Germany.5e7d912a-d474-11eb-a588-f45c89abb0d9"
+ "com.apple.TMobile_US.5904fc42-d474-11eb-9051-f45c89abb0d9"
+ "com.apple.TMobile_gr.5976b38c-d474-11eb-af2a-f45c89abb0d9"
+ "com.apple.TMobile_uk.490fec70-d474-11eb-93f4-f45c89abb0d9"
+ "com.apple.TMobile_uk.5f0fb780-d474-11eb-9b33-f45c89abb0d9"
+ "com.apple.Telenor_no.45fb9d86-d474-11eb-bb98-f45c89abb0d9"
+ "com.apple.Telenor_no.5ae4b7c8-d474-11eb-ac49-f45c89abb0d9"
+ "com.apple.Telia_se.482486ea-d474-11eb-aebd-f45c89abb0d9"
+ "com.apple.Telia_se.482488f2-d474-11eb-aebd-f45c89abb0d9"
+ "com.apple.TrueH_th.43ebf112-d474-11eb-9b7d-f45c89abb0d9"
+ "com.apple.TrueH_th.579f01f4-d474-11eb-8625-f45c89abb0d9"
+ "com.apple.Verizon_LTE_US.44d722f4-d474-11eb-8194-f45c89abb0d9"
+ "com.apple.Verizon_LTE_US.592d64e8-d474-11eb-a7e5-f45c89abb0d9"
+ "com.apple.Verizon_LTE_US.592d6650-d474-11eb-a7e5-f45c89abb0d9"
+ "com.apple.Verizon_LTE_US.592d66b4-d474-11eb-a7e5-f45c89abb0d9"
+ "com.apple.Verizon_Response_LTE_US.5b78c5e4-d474-11eb-98d2-f45c89abb0d9"
+ "com.apple.Verizon_Response_LTE_US.5b78c7d8-d474-11eb-98d2-f45c89abb0d9"
+ "com.apple.Verizon_Response_LTE_US.5b78c846-d474-11eb-98d2-f45c89abb0d9"
+ "com.apple.VimpelCom_ru.577ac000-d474-11eb-b953-f45c89abb0d9"
+ "com.apple.Viva_kw.46df0a08-d474-11eb-acb5-f45c89abb0d9"
+ "com.apple.Vodafone_Cambio_uk.5852047a-d474-11eb-a1eb-f45c89abb0d9"
+ "com.apple.Vodafone_Cambio_uk.585205d8-d474-11eb-a1eb-f45c89abb0d9"
+ "com.apple.Vodafone_uk.4578dd74-d474-11eb-96b4-f45c89abb0d9"
+ "com.apple.Vodafone_uk.4578debe-d474-11eb-96b4-f45c89abb0d9"
+ "com.apple.Vodafone_uk.5a2a47ee-d474-11eb-9eb6-f45c89abb0d9"
+ "com.apple.Vodafone_uk.5a2a497e-d474-11eb-9eb6-f45c89abb0d9"
+ "com.apple.Zain_kw.496fdf22-d474-11eb-bbed-f45c89abb0d9"
+ "com.apple.Zain_kw.5fc0e848-d474-11eb-80ce-f45c89abb0d9"
+ "com.apple.Zain_sa.493051e0-d474-11eb-8295-f45c89abb0d9"
+ "com.apple.Zain_sa.4930532a-d474-11eb-8295-f45c89abb0d9"
+ "com.apple.Zain_sa.5f31e53a-d474-11eb-9afe-f45c89abb0d9"
+ "com.apple.Zain_sa.5f31e670-d474-11eb-9afe-f45c89abb0d9"
+ "com.apple.domains.7C25BE75-2C31-4897-A944-84B374708EEE"
+ "com.apple.dtac_th.486a3afa-d474-11eb-9b5d-f45c89abb0d9"
+ "com.apple.dtac_th.486a3cee-d474-11eb-9b5d-f45c89abb0d9"
+ "com.apple.dtac_th.5e5835f6-d474-11eb-8aa5-f45c89abb0d9"
+ "com.apple.dtac_th.5e5837a4-d474-11eb-8aa5-f45c89abb0d9"
+ "com.apple.du_Virgin_ae.440d0be0-d474-11eb-b255-f45c89abb0d9"
+ "com.apple.du_Virgin_ae.57c160aa-d474-11eb-8836-f45c89abb0d9"
+ "com.apple.du_ae.445070ec-d474-11eb-a6ad-f45c89abb0d9"
+ "com.apple.du_ae.58764b96-d474-11eb-9301-f45c89abb0d9"
+ "com.apple.mobile.carriersupport.wifi.indosat_id.com.apple.wifi.managed.51942931-F088-4553-A439-A5D5F8D18CD7"
+ "com.apple.mobile.carriersupport.wifi.indosat_id.com.apple.wifi.managed.68429129-85EC-401D-BAE8-5923B951AF6C"
+ "com.apple.mobily_sa.463bc0be-d474-11eb-944c-f45c89abb0d9"
+ "com.apple.mobily_sa.463bc1ea-d474-11eb-944c-f45c89abb0d9"
+ "com.apple.mobily_sa.463bc244-d474-11eb-944c-f45c89abb0d9"
+ "com.apple.mobily_sa.6F192B81-6FF6-41FB-BFB4-F59A677ADE8F"
+ "com.apple.mobily_sa.9ECA6301-FC5F-4060-BD2D-1D36D8B28251"
+ "com.apple.mobily_sa.C624E1ED-10CF-403C-B769-942203E23F8E"
+ "com.apple.security.root.6965949E-1076-4842-9ADD-965C5E6D0358"
+ "com.apple.security.root.C6D8E2D4-F1B4-437B-81AF-401D53E30707"
+ "com.apple.wifi.managed.01455DDE-4BF5-4493-B3BC-66AB9E10CDBF"
+ "com.apple.wifi.managed.04AD4ACD-0030-4266-8BEF-1312288CF029"
+ "com.apple.wifi.managed.11A235FC-D8AF-4B5A-A38E-23D10F173E9E"
+ "com.apple.wifi.managed.1f48f7d8-da0a-11eb-a4c7-f45c89abb0d9"
+ "com.apple.wifi.managed.1f48f940-da0a-11eb-a4c7-f45c89abb0d9"
+ "com.apple.wifi.managed.220D37DB-24E5-41AB-98E3-41CC696D1DEE"
+ "com.apple.wifi.managed.28041096-10FA-410B-B9D8-5EBBFA63F8A5"
+ "com.apple.wifi.managed.33A3FD53-5E90-4AE8-B05F-5D9B8259CDF5"
+ "com.apple.wifi.managed.35AA53A3-E310-4427-A4BA-6BB1F90A9370"
+ "com.apple.wifi.managed.390E9A07-92DF-4946-A33C-2A05CDA8DA90"
+ "com.apple.wifi.managed.5198E899-6CA9-498F-A459-601459B141F2"
+ "com.apple.wifi.managed.7128D899-6CA9-498F-A459-601459B15203"
+ "com.apple.wifi.managed.71CB0883-2F04-478E-BD3E-37EF4D38E03A"
+ "com.apple.wifi.managed.7656622A-3D51-44D7-BD65-B5DB3434B3F9"
+ "com.apple.wifi.managed.7C04AD5A-3FC1-4FC1-A5BA-8709CA74CDAE"
+ "com.apple.wifi.managed.9D09CCDE-A847-4B8B-80EF-532629E2B5FB"
+ "com.apple.wifi.managed.AA4A353D-44D3-46E3-A801-7132A4417A24"
+ "com.apple.wifi.managed.AFCFACD2-1AE0-43CD-B7AC-F1E9BFC58D55"
+ "com.apple.wifi.managed.AFD5FC87-EBD9-47E6-B387-BA1645C70BEA"
+ "com.apple.wifi.managed.B781ADBA-95BE-4D1C-A52B-2DDD3C9F9CD1"
+ "com.apple.wifi.managed.BB345DDE-4BF5-4493-B3BA-66AB9E10CDBC"
+ "com.apple.wifi.managed.EC565CCD-4BF5-4493-B3BC-66AB9E10CDBC"
+ "com.apple.wifi.managed.F0345CCD-4BF5-4493-B3BC-66AB9E10CDBC"
+ "com.apple.wifi.managed.F0345DDE-4BF5-4493-B3BC-66AB9E10CDBE"
+ "com.apple.wifi.managed.F0345DDE-4BF5-4493-B3BC-66AB9E10CDCA"
+ "com.apple.wifi.managed.F405AF22-DC47-480B-A79C-51039C351000"
+ "com.apple.wifi.managed.F6901E6F-8C5C-42FA-8A35-BA30EDA033B2"
+ "com.apple.wifi.managed.FB445CCD-4BF5-4493-B3BC-66AB9E10CDBC"
+ "deviceAccessAuthorizationNotifyToken"
+ "getAuthorizedDevices:"
+ "getDevicesWithFlags:session:error:"
+ "setDeviceAccessAuthorizationNotifyToken:"
- "@\"DASession\""
- "T@\"DASession\",&,V_deviceAccessSession"
- "TB,V_deviceAccessSessionActivated"
- "[corewifi] [wifi-network-sharing] DeviceAccess session event (%{public}@)"
- "[corewifi] [wifi-network-sharing] Failed to activate device access session (error=%{public}@)"
- "[corewifi] [wifi-network-sharing] Successfully activated device access session"
- "__activateDeviceAccessSessionWithCompletion:"
- "_deviceAccessSession"
- "_deviceAccessSessionActivated"
- "availableDevices"
- "carrierPayloadIdentifier=%@, "
- "com.apple.Softbank_jp.535f95d6-d474-11eb-af6d-f45c89abb0d9"
- "com.apple.TIM_br.4c405a6a-d474-11eb-92d1-f45c89abb0d9"
- "com.apple.wifi.managed.4088E899-6CA9-498F-A459-601459B141F2"
- "com.apple.wifi.managed.5018D899-6CA9-498F-A459-601459B15203"
- "com.apple.wifi.managed.5FAA0883-2F04-478E-BD3E-37EF4D38E03A"
- "com.apple.wifi.managed.AA245DDE-4BF5-4493-B3BA-66AB9E10CDBC"
- "com.apple.wifi.managed.BB245DDE-4BF5-4493-B3BA-66AB9E10CDBC"
- "com.apple.wifi.managed.CA465CCD-4BF5-4493-B3BC-66AB9E10CDBC"
- "com.apple.wifi.managed.E395AF22-DC47-480B-A79C-51039C351000"
- "com.apple.wifi.managed.E9245CCD-4BF5-4493-B3BC-66AB9E10CDBC"
- "com.apple.wifi.managed.E9245DDE-4BF5-4493-B3BC-66AB9E10CDBD"
- "com.apple.wifi.managed.E9245DDE-4BF5-4493-B3BC-66AB9E10CDBE"
- "com.apple.wifi.managed.E9245DDE-4BF5-4493-B3BC-66AB9E10CDBF"
- "com.apple.wifi.managed.E9245DDE-4BF5-4493-B3BC-66AB9E10CDCA"
- "com.apple.wifi.managed.EA345CCD-4BF5-4493-B3BC-66AB9E10CDBC"
- "device"
- "deviceAccessSession"
- "deviceAccessSessionActivated"
- "eventType"
- "setDeviceAccessSession:"
- "setDeviceAccessSessionActivated:"
- "setDeviceFlags:"
- "v16@?0@\"DAEvent\"8"

```
