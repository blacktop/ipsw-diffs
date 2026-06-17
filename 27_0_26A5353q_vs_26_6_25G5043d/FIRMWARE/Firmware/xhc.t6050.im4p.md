## xhc.t6050.im4p

> `Firmware/xhc.t6050.im4p`

```diff

 
-  __TEXT.__text: 0x15d08 sha256:6cc3e55c74e2650c5217e3ba85cfa1d19bbf00e76e491a84532ca9a3001721c6
-  __TEXT._rtk_vtor: 0x300 sha256:94786d8bce01f7bdb2d98314eb090601c635a51183c6e1e118ef27cb5530e6ae
-  __TEXT.__const: 0x7d4 sha256:5774d1e0c75f9cb1234a13e768cabf709a02215cd69a5ef363b6eca792aaf278
-  __TEXT._rtk_mtab: 0x194 sha256:7b5d64560bf544818141279bc4638fe9dceb8425935235a3e60b33d918e5dd23
-  __TEXT.__cstring: 0x1a5f sha256:dbf4416c098f61476c823a63ea4dcc2bb09ca973197aa8fbc0f7e4694d90c2af
+  __TEXT.__text: 0x15f98 sha256:92dd825458b4b9ac6949e55b0c39d4212e7f20412eaaf73c74a93a005f14e3c1
+  __TEXT._rtk_vtor: 0x300 sha256:0121c4fd5304c547a2a6b368acccd3251b1e4186ca9f9987676615034fabd5af
+  __TEXT.__const: 0xbf0 sha256:b48f702da0d9c12d66bcdad311649a4218da44692edf5353c0394c89869e63a2
+  __TEXT._rtk_mtab: 0x194 sha256:9765960b524a11bbc439756ed36f7f8e4c2a97b5a7efad3d89de530bdd354105
+  __TEXT.__cstring: 0x1b48 sha256:6e1c5b9de870ddeae871747063461215c87bc8cb2efcbc10492f0235bc373a27
   __TEXT.__constructor: 0x0
-  __TEXT.__rebase_info: 0x1fc sha256:85e2d2ddb5e3d28f40f9371465e04e41ac6d13d024c934e5564981d72fba9a8a
+  __TEXT.__rebase_info: 0x204 sha256:227ff9f21deebd1b8341824478706e7cc07ac675e953d2113aae768ba65ef6cd
   __DATA._rtk_power: 0x7c sha256:6be6c20e6ba2cdeae8716bf2496185bce47d6d380d22ae1f3b125703c2474d0b
-  __DATA.__const: 0x5f0 sha256:6b49df664df26b2b767592660106695000ff0dff944d9c1e6f33778997d10c56
-  __DATA.__data: 0xfe8 sha256:507242fddb9d18129e12d125431373b969b7d06d0f380a05dd717d3b2265fd39
-  __DATA._rtk_patchbay: 0x131 sha256:e728eab4c534f8654f392529a7f210a99e5a7df945ef43cf27c74b0b227fd444
-  __DATA.__nl_symbol_ptr: 0x5c sha256:a9f9ca37f0222ef003778b5f8931c985f31ad728f502de9ee8b4270d950fa471
+  __DATA.__const: 0x608 sha256:b7b8d124644ad12ffb8d982baaf203632bb12fbf461740a87a53566983594c32
+  __DATA.__data: 0xff0 sha256:3cb824875a02430032a05fbdfd5ae5230def91eb617cc3444c37f728d9439890
+  __DATA._rtk_patchbay: 0x131 sha256:552f11e0e791aef0921c84dc3588c72c1ab481c33b5c38054b83a8c211630904
+  __DATA.__nl_symbol_ptr: 0x5c sha256:2c6b59209f0359356994e4c19adf6b37ccc28465f8892a1c859e471262076d85
   __DATA.__mod_init_func: 0x0
   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
-  __DATA.__zerofill: 0xf718 sha256:7a0633855edf9cbc71f72294b987454ebfd4dc9cf0d9aca10db8404f8d99616d
-  __OS_LOG.__string: 0x250d sha256:743b37af486abf357526ffe62aa867d45a1fda95fa29e7d8f3fbe24562dfd7f7
-  __VTOR._rtk_vtor_patch: 0x90 sha256:14c592982ad03c2b5a7c68c719c86708ef58804475e058d6bdc194f6322f2662
-  UUID: 68E05903-FD2A-3D01-A400-70D46C405C03
+  __DATA.__zerofill: 0xfab0 sha256:e88b149724d71a6e75fc2567066c42eb9c1ee202ec694067f88fede7f547a553
+  __OS_LOG.__string: 0x2467 sha256:643a573037a62b362bedbaf78a113bf37bbe91432aee148ed1e22398f005a533
+  __VTOR._rtk_vtor_patch: 0x90 sha256:ef4747e2944cbd80cba0c7fb6fc33837831977ece85614c07bcf26117f758940
+  UUID: 9D8EB4FC-35C0-399B-BEB0-D2788A50C258
   Functions: 0
   Symbols:   0
-  CStrings:  386
+  CStrings:  391
 
CStrings:
+ "(16)"
+ "(CAP_REGS)->rdi_mapped && !(CAP_REGS)->rdi_mmio_handler_valid"
+ "XHC FW SYSLOG Handling NOP\n"
+ "[XHC FW] Soc Rev mimatch detected! controller is about to be non-functional!"
+ "async_scheduler.c"
+ "capability_registers.c"
+ "commands.c:177::@XHCAddrTag(%08x) Send Set Address: ERROR @Enum(internal_fw_event_type_t(%u))"
+ "commands.c:249::@XHCAddrTag(%08x) Address Device: BSR=%u"
+ "commands.c:264::@XHCAddrTag(%08x) ERROR: Port state is not in U0"
+ "commands.c:414::@XHCAddrTag(%08x) ERROR: Invalid EP Context. max_packet_size=%u, max_burst_size=%u, endpoint_type=@Enum(endpoint_type_t(%u))"
+ "commands.c:420::@XHCAddrTag(%08x) ERROR: Evaluate context while EP State = @Enum(endpoint_state_t(%u))"
+ "commands.c:459::@XHCAddrTag(%08x) Invalid EP context - input EP state is not disabled"
+ "commands.c:464::@XHCAddrTag(%08x) Invalid EP context - Software is trying to add an endpoint without dropping its current resources"
+ "commands.c:469::@XHCAddrTag(%08x) Invalid EP context - Isoc endpoints are not supported"
+ "commands.c:474::@XHCAddrTag(%08x) Invalid EP context - interval = %u"
+ "commands.c:480::@XHCAddrTag(%08x) Invalid EP context - Software allocated more streams (%u) than supported"
+ "commands.c:485::@XHCAddrTag(%08x) Invalid EP context - Inavlid endpoint_type=@Enum(endpoint_type_t(%u)) for streaming"
+ "commands.c:490::@XHCAddrTag(%08x) Invalid EP context - AUSS only Linear Stream Array (LSA) mode is supported."
+ "commands.c:496::@XHCAddrTag(%08x) Invalid EP context - Inavlid average_trb_length=0."
+ "commands.c:502::@XHCAddrTag(%08x) Invalid EP context - max_packet_size=%u, max_burst_size=%u, endpoint_type=@Enum(endpoint_type_t(%u))"
+ "commands.c:524::@XHCAddrTag(%08x) Configure Endpoint: deconfigure=%u"
+ "commands.c:648::@XHCAddrTag(%08x) Stop Endpoint Command Handler"
+ "commands.c:657::@XHCAddrTag(%08x) Wrong Endpoint State: @Enum(endpoint_state_t(%u))"
+ "commands.c:684::@XHCAddrTag(%08x) Set TR DQ PTR: dq_ptr=0x%llx dcs=%u"
+ "commands.c:72::@XHCAddrTag(%08x) Signaling Set Address Completion"
+ "commands.c:737::Handling NoOp w/ execution_time_usec=%u busy_wait=%u"
+ "commands.c:794::@XHCAddrTag(%08x) Reset Endpoint: TSP=%u"
+ "commands.c:804::@XHCAddrTag(%08x) Reset EP: Invalid Output context EP State: Output=@Enum(endpoint_state_t(%u))"
+ "commands.c:815::@XHCAddrTag(%08x) Reset EP: Invalid DBL EP State: @Enum(endpoint_state_t(%u))"
+ "commands.c:82::@XHCAddrTag(%08x) Send Set Address, address=%u"
+ "commands.c:865::@XHCAddrTag(%08x) Slot Not Enabled Error!"
+ "commands.c:897::@XHCAddrTag(%08x) Invalid Slot State: slot_state=@Enum(slot_state_t(%u))"
+ "commands.c:908::Got Invalid Slot ID slot_id=%u"
+ "endpoint.c:330::@XHCAddrTag(%08x) Wait EP for no outstandings"
+ "endpoint.c:339::@XHCAddrTag(%08x) Wait EP for no flow control"
+ "endpoint.c:343::@XHCAddrTag(%08x) Wait EP for no DB outstandings failed due to @Enum(RTK_status(%u))"
+ "endpoint.c:391::@XHCAddrTag(%08x) stop endpoint request aborted"
+ "endpoint.c:421::Endpoint Update Stream Context: Invalid stream ID - internal_endpoint_id=%u, latest_stream_id=%u, #streams=%u"
+ "endpoint.c:533::@XHCAddrTag(%08x) Endpoint Stop Barrier Handler"
+ "endpoint.c:601::@XHCAddrTag(%08x) Endpoint Pre Stop Request"
+ "endpoint.c:659::@XHCAddrTag(%08x) Endpoint Post Stop Request, Status = @Enum(RTK_status(%u))"
+ "endpoint.c:708::@XHCAddrTag(%08x) Endpoint Stop Request"
+ "endpoint.c:711::@XHCAddrTag(%08x) Skip Endpoint Stop Request, Pre Stop Status = @Enum(RTK_status(%u))"
+ "endpoint.c:740::@XHCAddrTag(%08x) Endpoint Set TR DQPTR: Invalid stream ID, latest_stream_id=%u, #streams=%u"
+ "endpoint.c:753::@XHCAddrTag(%08x) DB Ring to stopped EP"
+ "endpoint.c:781::@XHCAddrTag(%08x) Flush Stop EP, completion_code=@Enum(trb_completion_code_t(%u))"
+ "endpoint.c:794::@XHCAddrTag(%08x) Warning! endpoint_flush_stop_ep_event_handler received unexpected stop endpoint completion event"
+ "event_ring.c:132::@Enum(event_ring_index_t(%u)): send event: trb type: @Enum(trb_type_t(%u)), completion code: @Enum(trb_completion_code_t(%u))"
+ "event_ring.c:200::Update ER=@Enum(event_ring_index_t(%u)) Segment"
+ "has_supported_chip"
+ "has_supported_chip_rev"
+ "internal_fw_event.c:117::Internal FW Events: signaled during timeout"
+ "main.c:32::XHC firmware started (FW build version: AppleXHCFirmware-141.100.96~644.t6050)"
+ "platform.c:120::crashlog completed"
+ "platform.c:70::Chip: t%04x, Variant: @Enum(tunableh_chip_variant_t(%u)), Revision: %c%x"
+ "port.c:127::@XHCAddrTag(%08x) Port Configure: Port already configured and mapped with slot=%u"
+ "port.c:141::@XHCAddrTag(%08x) Port Configure: Error due to race w/ barrier get_connector_num_status=@Enum(RTK_status(%u)) capture_speed_status=@Enum(RTK_status(%u))"
+ "run_stop.c:140::@BlockTagBeginRunStop current_state=@Enum(hc_state_t(%u)) , rs_bit=%u"
+ "run_stop.c:152::@BlockTagDoneRunStop current_state=@Enum(hc_state_t(%u)) status=@Enum(RTK_status(%u))"
+ "run_stop.c:60::RS Unhandled Barrier Handler: ports_not_in_u0_permit_bitmap=0x%x"
+ "save_restore.c:214::Save Restore Controller State, HC not halted. @Enum(save_restore_command_t(%u)) aborted"
+ "save_restore.c:224::Save Restore Controller State, prepare context failed. status=@Enum(RTK_status(%u))"
+ "save_restore.c:230::@BlockTagBeginSaveRestore cmd=@Enum(save_restore_command_t(%u))"
+ "save_restore.c:242::@BlockTagDoneSaveRestore status=@Enum(RTK_status(%u))"
+ "syslog"
+ "tunableh_chip_family.c"
+ "xhc_reset.c:42::XHC reset"
- "%s:%d About to wait on an unregistered event"
- "(4)"
- "16"
- "commands.c:176::@XHCAddrTag(%08x) Send Set Address: ERROR @Enum(internal_fw_event_type_t(%u))"
- "commands.c:248::@XHCAddrTag(%08x) Address Device: BSR=%u"
- "commands.c:263::@XHCAddrTag(%08x) ERROR: Port state is not in U0"
- "commands.c:413::@XHCAddrTag(%08x) ERROR: Invalid EP Context. max_packet_size=%u, max_burst_size=%u, endpoint_type=@Enum(endpoint_type_t(%u))"
- "commands.c:419::@XHCAddrTag(%08x) ERROR: Evaluate context while EP State = @Enum(endpoint_state_t(%u))"
- "commands.c:458::@XHCAddrTag(%08x) Invalid EP context - input EP state is not disabled"
- "commands.c:463::@XHCAddrTag(%08x) Invalid EP context - Software is trying to add an endpoint without dropping its current resources"
- "commands.c:468::@XHCAddrTag(%08x) Invalid EP context - Isoc endpoints are not supported"
- "commands.c:473::@XHCAddrTag(%08x) Invalid EP context - interval = %u"
- "commands.c:479::@XHCAddrTag(%08x) Invalid EP context - Software allocated more streams (%u) than supported"
- "commands.c:484::@XHCAddrTag(%08x) Invalid EP context - Inavlid endpoint_type=@Enum(endpoint_type_t(%u)) for streaming"
- "commands.c:489::@XHCAddrTag(%08x) Invalid EP context - AUSS only Linear Stream Array (LSA) mode is supported."
- "commands.c:495::@XHCAddrTag(%08x) Invalid EP context - Inavlid average_trb_length=0."
- "commands.c:501::@XHCAddrTag(%08x) Invalid EP context - max_packet_size=%u, max_burst_size=%u, endpoint_type=@Enum(endpoint_type_t(%u))"
- "commands.c:523::@XHCAddrTag(%08x) Configure Endpoint: deconfigure=%u"
- "commands.c:647::@XHCAddrTag(%08x) Stop Endpoint Command Handler"
- "commands.c:656::@XHCAddrTag(%08x) Wrong Endpoint State: @Enum(endpoint_state_t(%u))"
- "commands.c:683::@XHCAddrTag(%08x) Set TR DQ PTR: dq_ptr=0x%llx dcs=%u"
- "commands.c:71::@XHCAddrTag(%08x) Signaling Set Address Completion"
- "commands.c:736::Handling NoOp w/ execution_time_usec=%u busy_wait=%u"
- "commands.c:786::@XHCAddrTag(%08x) Reset Endpoint: TSP=%u"
- "commands.c:796::@XHCAddrTag(%08x) Reset EP: Invalid Output context EP State: Output=@Enum(endpoint_state_t(%u))"
- "commands.c:807::@XHCAddrTag(%08x) Reset EP: Invalid DBL EP State: @Enum(endpoint_state_t(%u))"
- "commands.c:81::@XHCAddrTag(%08x) Send Set Address, address=%u"
- "commands.c:857::@XHCAddrTag(%08x) Slot Not Enabled Error!"
- "commands.c:889::@XHCAddrTag(%08x) Invalid Slot State: slot_state=@Enum(slot_state_t(%u))"
- "commands.c:900::Got Invalid Slot ID slot_id=%u"
- "endpoint.c:331::@XHCAddrTag(%08x) Wait EP for no outstandings"
- "endpoint.c:340::@XHCAddrTag(%08x) Wait EP for no flow control"
- "endpoint.c:344::@XHCAddrTag(%08x) Wait EP for no DB outstandings failed due to @Enum(RTK_status(%u))"
- "endpoint.c:392::@XHCAddrTag(%08x) stop endpoint request aborted"
- "endpoint.c:422::Endpoint Update Stream Context: Invalid stream ID - internal_endpoint_id=%u, latest_stream_id=%u, #streams=%u"
- "endpoint.c:534::@XHCAddrTag(%08x) Endpoint Stop Barrier Handler"
- "endpoint.c:603::@XHCAddrTag(%08x) Endpoint Pre Stop Request"
- "endpoint.c:661::@XHCAddrTag(%08x) Endpoint Post Stop Request, Status = @Enum(RTK_status(%u))"
- "endpoint.c:710::@XHCAddrTag(%08x) Endpoint Stop Request"
- "endpoint.c:713::@XHCAddrTag(%08x) Skip Endpoint Stop Request, Pre Stop Status = @Enum(RTK_status(%u))"
- "endpoint.c:742::@XHCAddrTag(%08x) Endpoint Set TR DQPTR: Invalid stream ID, latest_stream_id=%u, #streams=%u"
- "endpoint.c:755::@XHCAddrTag(%08x) DB Ring to stopped EP"
- "endpoint.c:783::@XHCAddrTag(%08x) Flush Stop EP, completion_code=@Enum(trb_completion_code_t(%u))"
- "endpoint.c:796::@XHCAddrTag(%08x) Warning! endpoint_flush_stop_ep_event_handler received unexpected stop endpoint completion event"
- "event_ring.c:136::@Enum(event_ring_index_t(%u)): send event: trb type: @Enum(trb_type_t(%u)), completion code: @Enum(trb_completion_code_t(%u))"
- "event_ring.c:204::Update ER=@Enum(event_ring_index_t(%u)) Segment"
- "internal_fw_event.c:120::Internal FW Events: signaled during timeout"
- "main.c:32::XHC firmware started (FW build version: AppleXHCFirmware-241~284.t6050)"
- "platform.c:101::[XHC FW] Soc Rev mimatch detected! controller is about to be non-functional!"
- "platform.c:133::crashlog completed"
- "platform.c:66::Chip: t%04x, Variant: @Enum(tunableh_chip_variant_t(%u)), Revision: %c%x"
- "port.c:126::@XHCAddrTag(%08x) Port Configure: Port already configured and mapped with slot=%u"
- "port.c:140::@XHCAddrTag(%08x) Port Configure: Error due to race w/ barrier get_connector_num_status=@Enum(RTK_status(%u)) capture_speed_status=@Enum(RTK_status(%u))"
- "run_stop.c:148::@BlockTagBeginRunStop current_state=@Enum(hc_state_t(%u)) , rs_bit=%u"
- "run_stop.c:160::@BlockTagDoneRunStop current_state=@Enum(hc_state_t(%u)) status=@Enum(RTK_status(%u))"
- "run_stop.c:61::RS Unhandled Barrier Handler: ports_not_in_u0_permit_bitmap=0x%x"
- "save_restore.c:222::Save Restore Controller State, HC not halted. @Enum(save_restore_command_t(%u)) aborted"
- "save_restore.c:232::Save Restore Controller State, prepare context failed. status=@Enum(RTK_status(%u))"
- "save_restore.c:238::@BlockTagBeginSaveRestore cmd=@Enum(save_restore_command_t(%u))"
- "save_restore.c:250::@BlockTagDoneSaveRestore status=@Enum(RTK_status(%u))"
- "xhc_reset.c:104::@BlockTagDoneHCReset status=@Enum(RTK_status(%u))"
- "xhc_reset.c:95::@BlockTagBeginHCReset "

```
