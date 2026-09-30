## PerfPowerServicesReader

> `/System/Library/PrivateFrameworks/PerfPowerServicesReader.framework/PerfPowerServicesReader`

```diff

 2964.2.4.0.0
-  __TEXT.__text: 0x132028
+  __TEXT.__text: 0x138070
   __TEXT.__auth_stubs: 0xf30
   __TEXT.__init_offsets: 0xdc
-  __TEXT.__objc_methlist: 0x127d4
+  __TEXT.__objc_methlist: 0x12ba4
   __TEXT.__const: 0x5ffe
-  __TEXT.__cstring: 0xc037
+  __TEXT.__cstring: 0xc36b
   __TEXT.__gcc_except_tab: 0x4ad0
   __TEXT.__oslogstring: 0xdc2
-  __TEXT.__unwind_info: 0x4738
+  __TEXT.__unwind_info: 0x47b8
   __TEXT.__eh_frame: 0x98
-  __TEXT.__objc_classname: 0x1963
-  __TEXT.__objc_methname: 0x19530
-  __TEXT.__objc_methtype: 0x2748
-  __TEXT.__objc_stubs: 0x97e0
-  __DATA_CONST.__got: 0xa80
-  __DATA_CONST.__const: 0x28e0
-  __DATA_CONST.__objc_classlist: 0x548
+  __TEXT.__objc_classname: 0x199e
+  __TEXT.__objc_methname: 0x19622
+  __TEXT.__objc_methtype: 0x2771
+  __TEXT.__objc_stubs: 0x9860
+  __DATA_CONST.__got: 0xa90
+  __DATA_CONST.__const: 0x29d8
+  __DATA_CONST.__objc_classlist: 0x558
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5d70
+  __DATA_CONST.__objc_selrefs: 0x5da8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x4c0
+  __DATA_CONST.__objc_superrefs: 0x4d0
   __DATA_CONST.__objc_arraydata: 0x110
   __AUTH_CONST.__auth_got: 0x7b0
   __AUTH_CONST.__const: 0x30d0
-  __AUTH_CONST.__cfstring: 0xdca0
-  __AUTH_CONST.__objc_const: 0x165a8
+  __AUTH_CONST.__cfstring: 0xe280
+  __AUTH_CONST.__objc_const: 0x16a38
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x2990
+  __AUTH.__objc_data: 0x2a30
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x10ac
+  __DATA.__objc_ivar: 0x10e4
   __DATA.__data: 0x581
   __DATA.__bss: 0x38
   __DATA_DIRTY.__objc_data: 0xb40

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 4873E878-B88E-378A-83AD-80FF57368746
-  Functions: 7737
-  Symbols:   20917
-  CStrings:  8159
+  UUID: 7CA73EDF-6A5E-3029-86D1-FFDCE0F154E0
+  Functions: 7820
+  Symbols:   21112
+  CStrings:  8265
 
Symbols:
+ +[AWDMETRICSCellularPowerLog cellularRfTunerHistType]
+ +[AWDMETRICSCellularRfTunerHist tunerStateDurationType]
+ -[AWDMETRICSCellularPowerLog addCellularRfTunerHist:]
+ -[AWDMETRICSCellularPowerLog cellularRfTunerHistAtIndex:]
+ -[AWDMETRICSCellularPowerLog cellularRfTunerHistsCount]
+ -[AWDMETRICSCellularPowerLog cellularRfTunerHists]
+ -[AWDMETRICSCellularPowerLog clearCellularRfTunerHists]
+ -[AWDMETRICSCellularPowerLog setCellularRfTunerHists:]
+ -[AWDMETRICSCellularRfTunerHist .cxx_destruct]
+ -[AWDMETRICSCellularRfTunerHist addTunerStateDuration:]
+ -[AWDMETRICSCellularRfTunerHist clearTunerStateDurations]
+ -[AWDMETRICSCellularRfTunerHist copyTo:]
+ -[AWDMETRICSCellularRfTunerHist copyWithZone:]
+ -[AWDMETRICSCellularRfTunerHist description]
+ -[AWDMETRICSCellularRfTunerHist dictionaryRepresentation]
+ -[AWDMETRICSCellularRfTunerHist ftQualInd]
+ -[AWDMETRICSCellularRfTunerHist hasFtQualInd]
+ -[AWDMETRICSCellularRfTunerHist hasSubsId]
+ -[AWDMETRICSCellularRfTunerHist hasTimestamp]
+ -[AWDMETRICSCellularRfTunerHist hash]
+ -[AWDMETRICSCellularRfTunerHist isEqual:]
+ -[AWDMETRICSCellularRfTunerHist mergeFrom:]
+ -[AWDMETRICSCellularRfTunerHist readFrom:]
+ -[AWDMETRICSCellularRfTunerHist setFtQualInd:]
+ -[AWDMETRICSCellularRfTunerHist setHasFtQualInd:]
+ -[AWDMETRICSCellularRfTunerHist setHasSubsId:]
+ -[AWDMETRICSCellularRfTunerHist setHasTimestamp:]
+ -[AWDMETRICSCellularRfTunerHist setSubsId:]
+ -[AWDMETRICSCellularRfTunerHist setTimestamp:]
+ -[AWDMETRICSCellularRfTunerHist setTunerStateDurations:]
+ -[AWDMETRICSCellularRfTunerHist subsId]
+ -[AWDMETRICSCellularRfTunerHist timestamp]
+ -[AWDMETRICSCellularRfTunerHist tunerStateDurationAtIndex:]
+ -[AWDMETRICSCellularRfTunerHist tunerStateDurationsCount]
+ -[AWDMETRICSCellularRfTunerHist tunerStateDurations]
+ -[AWDMETRICSCellularRfTunerHist writeTo:]
+ -[AWDMETRICSTunerStateDuration StringAsRat:]
+ -[AWDMETRICSTunerStateDuration StringAsScenarioDecision:]
+ -[AWDMETRICSTunerStateDuration StringAsTxBand:]
+ -[AWDMETRICSTunerStateDuration copyTo:]
+ -[AWDMETRICSTunerStateDuration copyWithZone:]
+ -[AWDMETRICSTunerStateDuration description]
+ -[AWDMETRICSTunerStateDuration dictionaryRepresentation]
+ -[AWDMETRICSTunerStateDuration duration]
+ -[AWDMETRICSTunerStateDuration ftQualInd]
+ -[AWDMETRICSTunerStateDuration hasDuration]
+ -[AWDMETRICSTunerStateDuration hasFtQualInd]
+ -[AWDMETRICSTunerStateDuration hasPort]
+ -[AWDMETRICSTunerStateDuration hasRat]
+ -[AWDMETRICSTunerStateDuration hasScenarioDecision]
+ -[AWDMETRICSTunerStateDuration hasTxBand]
+ -[AWDMETRICSTunerStateDuration hasWorkMode]
+ -[AWDMETRICSTunerStateDuration hash]
+ -[AWDMETRICSTunerStateDuration isEqual:]
+ -[AWDMETRICSTunerStateDuration mergeFrom:]
+ -[AWDMETRICSTunerStateDuration port]
+ -[AWDMETRICSTunerStateDuration ratAsString:]
+ -[AWDMETRICSTunerStateDuration rat]
+ -[AWDMETRICSTunerStateDuration readFrom:]
+ -[AWDMETRICSTunerStateDuration scenarioDecisionAsString:]
+ -[AWDMETRICSTunerStateDuration scenarioDecision]
+ -[AWDMETRICSTunerStateDuration setDuration:]
+ -[AWDMETRICSTunerStateDuration setFtQualInd:]
+ -[AWDMETRICSTunerStateDuration setHasDuration:]
+ -[AWDMETRICSTunerStateDuration setHasFtQualInd:]
+ -[AWDMETRICSTunerStateDuration setHasPort:]
+ -[AWDMETRICSTunerStateDuration setHasRat:]
+ -[AWDMETRICSTunerStateDuration setHasScenarioDecision:]
+ -[AWDMETRICSTunerStateDuration setHasTxBand:]
+ -[AWDMETRICSTunerStateDuration setHasWorkMode:]
+ -[AWDMETRICSTunerStateDuration setPort:]
+ -[AWDMETRICSTunerStateDuration setRat:]
+ -[AWDMETRICSTunerStateDuration setScenarioDecision:]
+ -[AWDMETRICSTunerStateDuration setTxBand:]
+ -[AWDMETRICSTunerStateDuration setWorkMode:]
+ -[AWDMETRICSTunerStateDuration txBandAsString:]
+ -[AWDMETRICSTunerStateDuration txBand]
+ -[AWDMETRICSTunerStateDuration workMode]
+ -[AWDMETRICSTunerStateDuration writeTo:]
+ OBJC_IVAR_$_AWDMETRICSCellularPowerLog._cellularRfTunerHists
+ OBJC_IVAR_$_AWDMETRICSCellularRfTunerHist._ftQualInd
+ OBJC_IVAR_$_AWDMETRICSCellularRfTunerHist._has
+ OBJC_IVAR_$_AWDMETRICSCellularRfTunerHist._subsId
+ OBJC_IVAR_$_AWDMETRICSCellularRfTunerHist._timestamp
+ OBJC_IVAR_$_AWDMETRICSCellularRfTunerHist._tunerStateDurations
+ OBJC_IVAR_$_AWDMETRICSTunerStateDuration._duration
+ OBJC_IVAR_$_AWDMETRICSTunerStateDuration._ftQualInd
+ OBJC_IVAR_$_AWDMETRICSTunerStateDuration._has
+ OBJC_IVAR_$_AWDMETRICSTunerStateDuration._port
+ OBJC_IVAR_$_AWDMETRICSTunerStateDuration._rat
+ OBJC_IVAR_$_AWDMETRICSTunerStateDuration._scenarioDecision
+ OBJC_IVAR_$_AWDMETRICSTunerStateDuration._txBand
+ OBJC_IVAR_$_AWDMETRICSTunerStateDuration._workMode
+ _AWDMETRICSCellularRfTunerHistReadFrom
+ _AWDMETRICSTunerStateDurationReadFrom
+ _OBJC_CLASS_$_AWDMETRICSCellularRfTunerHist
+ _OBJC_CLASS_$_AWDMETRICSTunerStateDuration
+ _OBJC_METACLASS_$_AWDMETRICSCellularRfTunerHist
+ _OBJC_METACLASS_$_AWDMETRICSTunerStateDuration
+ __OBJC_$_CLASS_METHODS_AWDMETRICSCellularRfTunerHist
+ __OBJC_$_INSTANCE_METHODS_AWDMETRICSCellularRfTunerHist
+ __OBJC_$_INSTANCE_METHODS_AWDMETRICSTunerStateDuration
+ __OBJC_$_INSTANCE_VARIABLES_AWDMETRICSCellularRfTunerHist
+ __OBJC_$_INSTANCE_VARIABLES_AWDMETRICSTunerStateDuration
+ __OBJC_$_PROP_LIST_AWDMETRICSCellularRfTunerHist
+ __OBJC_$_PROP_LIST_AWDMETRICSTunerStateDuration
+ __OBJC_CLASS_PROTOCOLS_$_AWDMETRICSCellularRfTunerHist
+ __OBJC_CLASS_PROTOCOLS_$_AWDMETRICSTunerStateDuration
+ __OBJC_CLASS_RO_$_AWDMETRICSCellularRfTunerHist
+ __OBJC_CLASS_RO_$_AWDMETRICSTunerStateDuration
+ __OBJC_METACLASS_RO_$_AWDMETRICSCellularRfTunerHist
+ __OBJC_METACLASS_RO_$_AWDMETRICSTunerStateDuration
+ _objc_msgSend$addCellularRfTunerHist:
+ _objc_msgSend$cellularRfTunerHistAtIndex:
+ _objc_msgSend$cellularRfTunerHistsCount
+ _objc_msgSend$clearCellularRfTunerHists
CStrings:
+ "AWDMETRICSCellularRfTunerHist"
+ "AWDMETRICSTunerStateDuration"
+ "IDLE_MODE_SCENARIO"
+ "SYS_BAND_BC0"
+ "SYS_BAND_BC1"
+ "SYS_BAND_BC10"
+ "SYS_BAND_BC11"
+ "SYS_BAND_BC12"
+ "SYS_BAND_BC13"
+ "SYS_BAND_BC14"
+ "SYS_BAND_BC15"
+ "SYS_BAND_BC16"
+ "SYS_BAND_BC17"
+ "SYS_BAND_BC18"
+ "SYS_BAND_BC19"
+ "SYS_BAND_BC3"
+ "SYS_BAND_BC4"
+ "SYS_BAND_BC5"
+ "SYS_BAND_BC6"
+ "SYS_BAND_BC7"
+ "SYS_BAND_BC8"
+ "SYS_BAND_BC9"
+ "SYS_BAND_LTE_EUTRAN_BAND125"
+ "SYS_BAND_LTE_EUTRAN_BAND126"
+ "SYS_BAND_LTE_EUTRAN_BAND127"
+ "SYS_BAND_LTE_EUTRAN_BAND250"
+ "SYS_BAND_LTE_EUTRAN_BAND252"
+ "SYS_BAND_LTE_EUTRAN_BAND255"
+ "SYS_BAND_LTE_EUTRAN_BAND32"
+ "SYS_BAND_LTE_EUTRAN_BAND47"
+ "SYS_BAND_RESERVED_1"
+ "SYS_BAND_UMTS_BAND1"
+ "SYS_BAND_UMTS_BAND2"
+ "SYS_BAND_UMTS_BAND3"
+ "SYS_BAND_UMTS_BAND4"
+ "SYS_BAND_UMTS_BAND5"
+ "SYS_BAND_UMTS_BAND6"
+ "SYS_MODE_CDMA"
+ "SYS_MODE_CDMA_HDR"
+ "SYS_MODE_EHRPD"
+ "SYS_MODE_GW"
+ "SYS_MODE_GWL"
+ "SYS_MODE_HDR"
+ "SYS_MODE_LTE_V2"
+ "SYS_MODE_NR5G"
+ "SYS_MODE_SUSPENDED"
+ "SYS_MODE_UMTS"
+ "SYS_MODE_WLAN"
+ "T@\"NSMutableArray\",&,N,V_cellularRfTunerHists"
+ "_cellularRfTunerHists"
+ "addCellularRfTunerHist:"
+ "cellularRfTunerHist"
+ "cellularRfTunerHistAtIndex:"
+ "cellularRfTunerHistType"
+ "cellularRfTunerHists"
+ "cellularRfTunerHistsCount"
+ "clearCellularRfTunerHists"
+ "setCellularRfTunerHists:"
+ "{?=\"timestamp\"b1\"ftQualInd\"b1\"subsId\"b1}"

```
