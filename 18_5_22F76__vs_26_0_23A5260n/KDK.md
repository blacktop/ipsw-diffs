## KDKs

- `KDK_15.5_24F74.kdk/System/Library/Kernels/kernel.release.t8132`
- `KDK_26.0_25A5279m.kdk/System/Library/Kernels/kernel.release.t8132`

#### __block_literal_29

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- _Bool (ctid_t*);* __FuncPtr;	
+ bool (class OSObject*);* __FuncPtr;	
 struct __block_descriptor* __descriptor;	
-cond_swi_var_t cond;	
-uint64_t check_mask;	
-cond_swi_var64_s expected_cond;	
 }

```
#### __bounds_safety::wide_ptr.indexable.95

```diff

 struct __bounds_safety::wide_ptr.indexable.95 {
-void* ptr;	
-void* ub;	
+uint8_t* ptr;	
+uint8_t* ub;	
 }

```
#### nstat_detailed_counts

```c
struct nstat_detailed_counts {
  struct media_stats nstat_media_stats;
  u_int64_t          nstat_rxduplicatebytes;
  u_int64_t          nstat_rxoutoforderbytes;
  u_int64_t          nstat_txretransmit;
  u_int32_t          nstat_min_rtt;
  u_int32_t          nstat_avg_rtt;
  u_int32_t          nstat_var_rtt;
  u_int32_t          nstat_xtra_flags;
  uuid_t             nstat_xtra_uuid;
}

```
#### psemhashtable

```c
struct psemhashtable {
  struct psemhashhead *psem_table;
  u_long               psem_table_mask;
  uint8_t              psem_siphash_key[16];
}

```
#### proc

```diff

 uint32_t p_pth_tsd_offset;	
 user_addr_t p_stack_addr_hint;	
 _Atomic struct workqueue* p_wqptr;	
+_Atomic struct workq_aio_s* p_aio_wqptr;	
 struct timeval p_start;	
 void* p_rcall;	
 void* p_pthhash;	

```
#### __bounds_safety::wide_ptr.bidi_indexable.118

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.118 {
-struct nxctl_traffic_rule_generic_iocinfo* ptr;	
-struct nxctl_traffic_rule_generic_iocinfo* ub;	
-struct nxctl_traffic_rule_generic_iocinfo* lb;	
+struct __kern_buflet* ptr;	
+struct __kern_buflet* ub;	
+struct __kern_buflet* lb;	
 }

```
#### ifnet_traffic_descriptor_eth

```c
struct ifnet_traffic_descriptor_eth {
  struct ifnet_traffic_descriptor_common eth_common;
  ether_addr_t                           eth_raddr;
  uint16_t                               eth_type;
  uint8_t                                eth_mask;
}

```
#### IOService_StateNotificationItemCreate_Msg_With_Content

```diff

 IORPCMessageMach mach;	
 mach_msg_port_descriptor_t __object__descriptor;	
 mach_msg_ool_descriptor_t itemName__descriptor;	
-mach_msg_ool_descriptor_t schema__descriptor;	
+mach_msg_ool_descriptor_t value__descriptor;	
 struct IOService_StateNotificationItemCreate_Msg_Content content;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.37

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.37 {
-struct nexus_adapter* ptr;	
-struct nexus_adapter* ub;	
-struct nexus_adapter* lb;	
+char* ptr;	
+char* ub;	
+char* lb;	
 }

```
#### aop_tcp_info

```c
struct aop_tcp_info {
  struct tcp_info tcp_info;
  uint8_t         tcp_cc_algo;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.163

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.163 {
-struct cfil_msg_sock_stats* ptr;	
-struct cfil_msg_sock_stats* ub;	
-struct cfil_msg_sock_stats* lb;	
+struct nx_llink_info* ptr;	
+struct nx_llink_info* ub;	
+struct nx_llink_info* lb;	
 }

```
#### mkext_basic_header

```c
struct mkext_basic_header {
  uint32_t      magic;
  uint32_t      signature;
  uint32_t      length;
  uint32_t      adler32;
  uint32_t      version;
  uint32_t      numkexts;
  cpu_type_t    cputype;
  cpu_subtype_t cpusubtype;
}

```
#### __bounds_safety::wide_ptr.indexable.96

```diff

 struct __bounds_safety::wide_ptr.indexable.96 {
-char* ptr;	
-char* ub;	
+void* ptr;	
+void* ub;	
 }

```
#### static_if_key_true

```c
struct static_if_key_true {
  struct static_if_key key;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.2

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.2 {
-const u_int64_t* ptr;	
-const u_int64_t* ub;	
-const u_int64_t* lb;	
+struct nxctl_traffic_rule* ptr;	
+struct nxctl_traffic_rule* ub;	
+struct nxctl_traffic_rule* lb;	
 }

```
#### __bounds_safety::wide_ptr.indexable.200

```c
struct __bounds_safety::wide_ptr.indexable.200 {
  struct __kern_channel_ring *ptr;
  struct __kern_channel_ring *ub;
}

```
#### pthread_callbacks_s

```diff

  kern_return_t (thread_t, thread_state_t);* thread_set_wq_state64;	
  void ();* thread_exception_return;	
  void ();* thread_bootstrap_return;	
-void* __unused_was_absolutetime_to_microtime;	
+ void ();* abandon_preemption_disable_measurement;	
 void* __unused_was_thread_set_workq_pri;	
 void* __unused_was_thread_set_workq_qos;	
  struct uthread* (thread_t);* get_bsdthread_info;	

```
#### __bounds_safety::wide_ptr.bidi_indexable.241

```c
struct __bounds_safety::wide_ptr.bidi_indexable.241 {
  struct sockaddr_dl *ptr;
  struct sockaddr_dl *ub;
  struct sockaddr_dl *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.14

```c
struct __bounds_safety::wide_ptr.bidi_indexable.14 {
  char *ptr;
  char *ub;
  char *lb;
}

```
#### __block_literal_28

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- void ();* __FuncPtr;	
+ bool (class OSObject*);* __FuncPtr;	
 struct __block_descriptor_withcopydispose* __descriptor;	
 struct {
 void* __isa;	
 void* __forwarding;	
 int __flags;	
 int __size;	
-lck_rw_type_t lck_rw_type;	
+class IOUserServerCheckInToken* result;	
 }
-* lck_rw_type;	
-lck_rw_t* lock;	
+* result;	
+const class OSSymbol* serverName;	
 }

```
#### net_aop_capab_flow_stats

```c
struct net_aop_capab_flow_stats {
  uint32_t kaopcfs_version;
  void    *kaopcfs_prov_ctx;
  errno_t(void *, uint32_t, struct aop_flow_stats *);
  *kaopcfs_config;
}

```
#### __bounds_safety::wide_ptr.indexable.164

```c
struct __bounds_safety::wide_ptr.indexable.164 {
  void *ptr;
  void *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.131

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.131 {
-struct ip6_hdr* ptr;	
-struct ip6_hdr* ub;	
-struct ip6_hdr* lb;	
+struct user32_timeval* ptr;	
+struct user32_timeval* ub;	
+struct user32_timeval* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.139

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.139 {
-struct in6_ifaddr* ptr;	
-struct in6_ifaddr* ub;	
-struct in6_ifaddr* lb;	
+struct mbuf* ptr;	
+struct mbuf* ub;	
+struct mbuf* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.52

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.52 {
-struct skmem_obj_info* ptr;	
-struct skmem_obj_info* ub;	
-struct skmem_obj_info* lb;	
+const uint64_t* ptr;	
+const uint64_t* ub;	
+const uint64_t* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.141

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.141 {
-struct sk_stats_flow_adv* ptr;	
-struct sk_stats_flow_adv* ub;	
-struct sk_stats_flow_adv* lb;	
+struct ifclassq* ptr;	
+struct ifclassq* ub;	
+struct ifclassq* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.121

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.121 {
-struct __kern_packet* ptr;	
-struct __kern_packet* ub;	
-struct __kern_packet* lb;	
+uint64_t* ptr;	
+uint64_t* ub;	
+uint64_t* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.29

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.29 {
-struct __kern_quantum* ptr;	
-struct __kern_quantum* ub;	
-struct __kern_quantum* lb;	
+struct nx_pktq* ptr;	
+struct nx_pktq* ub;	
+struct nx_pktq* lb;	
 }

```
#### sock_cm_info

```c
struct sock_cm_info {
  int      sotc;
  int      netsvctype;
  uint64_t tx_time;
}

```
#### __bounds_safety::wide_ptr.indexable.133

```diff

 struct __bounds_safety::wide_ptr.indexable.133 {
-void* ptr;	
-void* ub;	
+struct flow_divert_group** ptr;	
+struct flow_divert_group** ub;	
 }

```
#### IOCircularDataQueueMemoryCursor

```c
struct IOCircularDataQueueMemoryCursor {
  uint32_t generation;
  uint32_t position;
  uint64_t sequenceNum;
}

```
#### zone_page_metadata

```diff

 zone_pva_t zm_page_prev;	
 }
  ;	
-vm_offset_t zm_pgz_orig_addr;	
-struct zone_page_metadata* zm_pgz_slot_next;	
 }
  ;	
 }

```
#### tcpstat

```diff

 u_int32_t tcps_pawsdrop;	
 u_int32_t tcps_predack;	
 u_int32_t tcps_preddat;	
-u_int32_t tcps_pcbcachemiss;	
 u_int32_t tcps_cachedrtt;	
 u_int32_t tcps_cachedrttvar;	
 u_int32_t tcps_cachedssthresh;	

 u_int32_t tcps_minmssdrops;	
 u_int32_t tcps_sndrexmitbad;	
 u_int32_t tcps_badrst;	
-u_int32_t tcps_sc_added;	
-u_int32_t tcps_sc_retransmitted;	
-u_int32_t tcps_sc_dupsyn;	
 u_int32_t tcps_sc_dropped;	
 u_int32_t tcps_sc_completed;	
-u_int32_t tcps_sc_bucketoverflow;	
-u_int32_t tcps_sc_cacheoverflow;	
-u_int32_t tcps_sc_reset;	
-u_int32_t tcps_sc_stale;	
 u_int32_t tcps_sc_aborted;	
-u_int32_t tcps_sc_badack;	
-u_int32_t tcps_sc_unreach;	
-u_int32_t tcps_sc_zonefail;	
 u_int32_t tcps_sc_sendcookie;	
 u_int32_t tcps_sc_recvcookie;	
-u_int32_t tcps_hc_added;	
-u_int32_t tcps_hc_bucketoverflow;	
 u_int32_t tcps_sack_recovery_episode;	
 u_int32_t tcps_sack_rexmits;	
 u_int32_t tcps_sack_rexmit_bytes;	

 u_int32_t tcps_snd_swcsum_bytes;	
 u_int32_t tcps_snd6_swcsum;	
 u_int32_t tcps_snd6_swcsum_bytes;	
-u_int32_t tcps_unused_1;	
-u_int32_t tcps_unused_2;	
-u_int32_t tcps_unused_3;	
 u_int32_t tcps_invalid_mpcap;	
 u_int32_t tcps_invalid_joins;	
 u_int32_t tcps_mpcap_fallback;	
 u_int32_t tcps_join_fallback;	
 u_int32_t tcps_estab_fallback;	
 u_int32_t tcps_invalid_opt;	
-u_int32_t tcps_mp_outofwin;	
 u_int32_t tcps_mp_reducedwin;	
 u_int32_t tcps_mp_badcsum;	
 u_int32_t tcps_mp_oodata;	

 u_int32_t tcps_detect_reordering;	
 u_int32_t tcps_delay_recovery;	
 u_int32_t tcps_avoid_rxmt;	
-u_int32_t tcps_unnecessary_rxmt;	
-u_int32_t tcps_nostretchack;	
-u_int32_t tcps_rescue_rxmt;	
 u_int32_t tcps_pto_in_recovery;	
 u_int32_t tcps_pmtudbh_reverted;	
-u_int32_t tcps_dsack_disable;	
 u_int32_t tcps_dsack_ackloss;	
 u_int32_t tcps_dsack_badrexmt;	
 u_int32_t tcps_dsack_sent;	
 u_int32_t tcps_dsack_recvd;	
 u_int32_t tcps_dsack_recvd_old;	
-u_int32_t tcps_mp_sel_symtomsd;	
 u_int32_t tcps_mp_sel_rtt;	
 u_int32_t tcps_mp_sel_rto;	
-u_int32_t tcps_mp_sel_peer;	
 u_int32_t tcps_mp_num_probes;	
 u_int32_t tcps_mp_verdowngrade;	
 u_int32_t tcps_drop_after_sleep;	

```
#### IOService_CreatePMAssertion_Msg

```c
struct IOService_CreatePMAssertion_Msg {
  IORPCMessageMach           mach;
  mach_msg_port_descriptor_t __object__descriptor;
}

```
#### __bounds_safety::wide_ptr.indexable.80

```diff

 struct __bounds_safety::wide_ptr.indexable.80 {
-uint8_t* ptr;	
-uint8_t* ub;	
+void* ptr;	
+void* ub;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.35

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.35 {
-struct kern_pbufpool_u_bkt* ptr;	
-struct kern_pbufpool_u_bkt* ub;	
-struct kern_pbufpool_u_bkt* lb;	
+struct __kern_quantum* ptr;	
+struct __kern_quantum* ub;	
+struct __kern_quantum* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.45

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.45 {
-uint32_t* ptr;	
-uint32_t* ub;	
-uint32_t* lb;	
+struct __metadata_preamble* ptr;	
+struct __metadata_preamble* ub;	
+struct __metadata_preamble* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.10

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.10 {
-struct skmem_cache* ptr;	
-struct skmem_cache* ub;	
-struct skmem_cache* lb;	
+void* ptr;	
+void* ub;	
+void* lb;	
 }

```
#### necp_flow_statistics

```c
struct necp_flow_statistics {
  union {
    struct tcp_info tcpi;
  } transport;
  uint8_t transport_proto;
  uint8_t pad[3];
}

```
#### __block_literal_35

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- void ();* __FuncPtr;	
-struct __block_descriptor* __descriptor;	
-lck_rw_t* lock;	
+ bool (class OSObject*);* __FuncPtr;	
+struct __block_descriptor_withcopydispose* __descriptor;	
+struct {
+void* __isa;	
+void* __forwarding;	
+int __flags;	
+int __size;	
+kern_return_t kr;	
+}
+* kr;	
+class IOService* this;	
+struct IOServiceStateChangeVars* ivars;	
+class IOStateNotificationListener* listener;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.120

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.120 {
-struct ifnet* ptr;	
-struct ifnet* ub;	
-struct ifnet* lb;	
+struct sk_stats_flow* ptr;	
+struct sk_stats_flow* ub;	
+struct sk_stats_flow* lb;	
 }

```
#### kd_dest

```c
struct kd_dest {
  kd_dest_kind_t kdd_kind;
  _Bool          kdd_chunk_format;
  off_t          kdd_cur_offset;
  union {
    struct {
      user_addr_t kdd_user_buffer;
      size_t      kdd_user_size;
    };
    struct {
      struct vfs_context kdd_vfs_ctx;
      vnode_t            kdd_vnode;
      off_t              kdd_file_written_since_flush;
    };
  };
}

```
#### skmem_sysctl

```diff

 int32_t path_mtu_discovery;	
 int32_t local_slowstart_flightsize;	
 uint32_t ecn_setup_percentage;	
-int32_t ecn_initiate_out;	
-int32_t ecn_negotiate_in;	
+int32_t ecn;	
 int32_t packetchain;	
 int32_t socket_unlocked_on_output;	
 int32_t min_iaj_win;	

 uint32_t microuptime_init;	
 uint32_t now_init;	
 uint32_t challengeack_limit;	
-int32_t do_rfc5961;	
 int32_t init_rtt_from_cache;	
 uint32_t autotunereorder;	
 uint32_t do_ack_compression;	
 uint32_t ack_compression_rate;	
-int32_t do_better_lr;	
 int32_t cubic_minor_fixes;	
 int32_t cubic_rfc_compliant;	
-int32_t aggressive_rcvwnd_inc;	
-int32_t ack_strategy;	
-int32_t flow_control_response;	
 int32_t randomize_timestamps;	
 uint32_t ledbat_plus_plus;	
 uint32_t use_ledbat;	

```
#### _CEKernelAPI

```c
struct _CEKernelAPI {
  CEReturn_t(const CEContextType_t, CEContext_t *, const uint8_t *, size_t);
  *contextInitWithType;
  CEReturn_t(const struct CERuntime *, const CEContextType_t, CEContext_t *,
             const uint8_t *, size_t);
  *contextInitWithTypeLegacy;
  CEReturn_t(const CEContext_t *, const void **);
  *contextGetLegacyContext;
  CEReturn_t(const CEContext_t *, const CEElement_t **);
  *contextGetDictionary;
  CEReturn_t(const CEContext_t *, const char *, CEElement_t *);
  *contextValueForKey;
  CEReturn_t(const CEContext_t *, const CEString_t *, CEElement_t *);
  *contextValueForKeyAsCEString;
  CEReturn_t(const CEContext_t *, const CEQuerySequence_t *, size_t,
             CEElement_t *);
  *contextExecuteQuery;
  CEReturn_t(const CEContext_t *, const CEContext_t *);
  *contextCheckSubset;
  CEReturn_t(const CEElement_t *, const CEElementIterate_t, void *);
  *elementIterate;
  CEReturn_t(const CEElement_t *, const CEDictionaryIterate_t, void *);
  *dictionaryIterate;
  CEReturn_t(const CEElement_t *, size_t *);
  *elementGetIndexCount;
  CEReturn_t(const CEElement_t *, size_t, CEElement_t *);
  *sequenceValueForIndex;
  CEReturn_t(const CEElement_t *, size_t, CEKeyValuePair_t *);
  *dictionaryValueForIndex;
  CEReturn_t(const CEElement_t *, const char *, CEElement_t *);
  *dictionaryValueForKey;
  CEReturn_t(const CEElement_t *, const CEString_t *, CEElement_t *);
  *dictionaryValueForKeyAsCEString;
  CEReturn_t(const CEElement_t *, CEType_t *);
  *elementGetType;
  CEReturn_t(const CEElement_t *, CEBuffer_t *);
  *elementGetCEBuffer;
  CEReturn_t(const CEElement_t *, CEBuffer_t *);
  *elementGetValueAsCEBuffer;
  CEReturn_t(const CEElement_t *, _Bool *);
  *elementGetBool;
  CEReturn_t(const CEElement_t *, int64_t *);
  *elementGetInteger;
  CEReturn_t(const CEElement_t *, CEString_t *);
  *elementGetString;
  CEReturn_t(const CEElement_t *, CEData_t *);
  *elementGetData;
  CEReturn_t(const CEElement_t *, _Bool);
  *elementMatchBool;
  CEReturn_t(const CEElement_t *, uint64_t);
  *elementMatchInteger;
  CEReturn_t(const CEElement_t *, const char *);
  *elementMatchString;
  CEReturn_t(const CEElement_t *, const CEString_t *);
  *elementMatchStringWithCEString;
  CEReturn_t(const CEElement_t *, const char *);
  *elementMatchStringWithWildcard;
  CEReturn_t(const CEElement_t *, const CEString_t *);
  *elementMatchStringWithCEStringAndWildcard;
  CEReturn_t(const CEElement_t *, const CEData_t *);
  *elementMatchData;
  CEReturn_t(const CEElement_t *, int64_t);
  *elementContainsInteger;
  CEReturn_t(const CEElement_t *, const char *);
  *elementContainsString;
  CEReturn_t(const CEElement_t *, const CEString_t *);
  *elementContainsStringWithCEString;
  CEReturn_t(const CEElement_t *, const char *);
  *elementContainsStringWithWildcard;
  CEReturn_t(const CEElement_t *, const CEString_t *);
  *elementContainsStringWithCEStringAndWildcard;
  CEReturn_t(const CEElement_t *, const CEData_t *);
  *elementContainsData;
  int32_t(const CEString_t *, const char *);
  *stringCompare;
  int32_t(const CEString_t *, const CEString_t *);
  *stringCompareWithCEString;
  int32_t(const CEString_t *, const char *);
  *stringComparePrefix;
  int32_t(const CEString_t *, const CEString_t *);
  *stringComparePrefixWithCEString;
  CEReturn_t(const CEElement_t *, const CEDictionaryIterateClosure_t);
  *dictionaryIterateWithClosure;
  CEReturn_t(const CEElement_t *, const CEElementIterateClosure_t);
  *elementIterateWithClosure;
  CEReturn_t(const CEContext_t *, size_t *);
  *contextEvaluateAcceleration;
  CEReturn_t(const CEContext_t *);
  *contextCheckAcceleration;
  CEReturn_t(CEContext_t *);
  *contextAccelerate;
  CEReturn_t(CEContext_t *);
  *contextDecelerate;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.212

```c
struct __bounds_safety::wide_ptr.bidi_indexable.212 {
  struct ifaddr *ptr;
  struct ifaddr *ub;
  struct ifaddr *lb;
}

```
#### memacct_statistics

```c
struct memacct_statistics {
  uint64_t peak;
  int64_t  allocated;
  uint64_t softlimit;
  uint64_t hardlimit;
  char     ma_name[16];
}

```
#### chreq

```diff

 uint32_t cr_pipe_id;	
 ring_id_t cr_ring_id;	
 ring_set_t cr_ring_set;	
-ch_endpoint_t cr_real_endpoint;	
 ch_endpoint_t cr_endpoint;	
 mach_vm_size_t cr_memsize;	
 mach_vm_offset_t cr_memoffset;	

```
#### _CSConfigOSPolicy

```diff

 struct _CSConfigOSPolicy {
 uint32_t minimumCodeDirectoryVersion;	
+uint8_t minimumHashTypeForPlatformCode;	
 _Bool trustCacheCodeOnly;	
 _Bool platformCodeOnly;	
 CMSPolicyFlags_t platformCTFlags;	

 CMSPolicyFlags_t appStoreQACTFlags;	
 CMSPolicyFlags_t profileValidatedQACTFlags;	
 CMSPolicyFlags_t profileCTFlags;	
+const char** developerLimit;	
 CSConfigFeatureSet_t featureSet;	
 struct {
 const char* appContainerPath;	

```
#### __bounds_safety::wide_ptr.indexable.109

```c
struct __bounds_safety::wide_ptr.indexable.109 {
  void *ptr;
  void *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.289

```c
struct __bounds_safety::wide_ptr.indexable.289 {
  struct necp_client_signable *ptr;
  struct necp_client_signable *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.154

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.154 {
-struct cfil_entry_stat* ptr;	
-struct cfil_entry_stat* ub;	
-struct cfil_entry_stat* lb;	
+struct netif_qset* ptr;	
+struct netif_qset* ub;	
+struct netif_qset* lb;	
 }

```
#### cfil_sign_parameters

```diff

 struct cfil_sign_parameters {
 struct cfil_crypto_state* csp_state;	
 struct cfil_crypto_data* csp_data;	
-struct __bounds_safety::wide_ptr.indexable.66 csp_signature;	
+struct __bounds_safety::wide_ptr.indexable.65 csp_signature;	
 uint32_t* csp_signature_size;	
 }

```
#### __bounds_safety::wide_ptr.indexable.192

```c
struct __bounds_safety::wide_ptr.indexable.192 {
  struct nstat_msg_src_update *ptr;
  struct nstat_msg_src_update *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.1

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.1 {
-struct skmem_slab* ptr;	
-struct skmem_slab* ub;	
-struct skmem_slab* lb;	
+struct skmem_cache* ptr;	
+struct skmem_cache* ub;	
+struct skmem_cache* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.186

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.186 {
-struct nstat_sysinfo_net_api_stats* ptr;	
-struct nstat_sysinfo_net_api_stats* ub;	
-struct nstat_sysinfo_net_api_stats* lb;	
+struct flow_mgr* ptr;	
+struct flow_mgr* ub;	
+struct flow_mgr* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.158

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.158 {
-struct nx_llink_info* ptr;	
-struct nx_llink_info* ub;	
-struct nx_llink_info* lb;	
+struct sadb_sastat* ptr;	
+struct sadb_sastat* ub;	
+struct sadb_sastat* lb;	
 }

```
#### nxctl_traffic_rule_eth_head

```c
struct nxctl_traffic_rule_eth_head {
  struct nxctl_traffic_rule_eth *slh_first;
}

```
#### necp_client_flow_registration

```diff

 u_int32_t flags;	
 unsigned int flow_result_read;	
 unsigned int defunct;	
+unsigned int aop_offload;	
 void* interface_handle;	
  void (void*, int, uint32_t, uint32_t, _Bool*);* interface_cb;	
 struct necp_client* client;	

```
#### __bounds_safety::wide_ptr.bidi_indexable.109

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.109 {
-struct flow_owner* ptr;	
-struct flow_owner* ub;	
-struct flow_owner* lb;	
+struct pkthdr* ptr;	
+struct pkthdr* ub;	
+struct pkthdr* lb;	
 }

```
#### __block_literal_34

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- void ();* __FuncPtr;	
-struct __block_descriptor_withcopydispose* __descriptor;	
-struct {
-void* __isa;	
-void* __forwarding;	
-int __flags;	
-int __size;	
-lck_rw_type_t lck_rw_type;	
-}
-* lck_rw_type;	
-lck_rw_t* lock;	
+ bool (class OSObject*);* __FuncPtr;	
+struct __block_descriptor* __descriptor;	
 }

```
#### nxctl_traffic_rule_eth_if_head

```c
struct nxctl_traffic_rule_eth_if_head {
  struct nxctl_traffic_rule_eth_if *slh_first;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.167

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.167 {
-struct nxprov_params* ptr;	
-struct nxprov_params* ub;	
-struct nxprov_params* lb;	
+uint8_t* ptr;	
+uint8_t* ub;	
+uint8_t* lb;	
 }

```
#### processor

```diff

 _Bool processor_online;	
 _Bool processor_inshutdown;	
 processor_offline_state_t processor_offline_state;	
+_Atomic int stir_the_pot_inbox_cpu;	
 }

```
#### pmap

```diff

 ledger_t ledger;	
 lck_rw_t rwlock;	
 queue_chain_t pmaps;	
-struct pmap* nested_pmap;	
 vm_map_address_t nested_region_addr;	
 vm_map_offset_t nested_region_size;	
 vm_map_offset_t nested_region_true_start;	
 vm_map_offset_t nested_region_true_end;	
+union {
+struct pmap* nested_pmap;	
 bitmap_t* nested_region_unnested_table_bitmap;	
+}
+ ;	
 os_ref_atomic_t ref_count;	
-uint32_t nested_no_bounds_refcnt;	
 union {
 uint16_t asid;	
 uint16_t vmid;	

 _Bool is_rosetta;	
 _Bool nx_enabled;	
 _Bool is_64bit;	
-_Bool nested_has_no_bounds_ref;	
-_Bool nested_bounds_set;	
 _Bool disable_jop;	
 _Bool xprr_tpro_enabled;	
 uint8_t type;	

```
#### __bounds_safety::wide_ptr.bidi_indexable.51

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.51 {
-struct __packet_opt* ptr;	
-struct __packet_opt* ub;	
-struct __packet_opt* lb;	
+struct __quantum* ptr;	
+struct __quantum* ub;	
+struct __quantum* lb;	
 }

```
#### netif_rx_flow_steering

```c
struct netif_rx_flow_steering {
  errno_t(void *, uint32_t, struct ifnet_traffic_descriptor_common *, uint32_t);
  *config_fn;
  void *prov_ctx;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.124

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.124 {
-struct __packet_opt* ptr;	
-struct __packet_opt* ub;	
-struct __packet_opt* lb;	
+struct __kern_packet* ptr;	
+struct __kern_packet* ub;	
+struct __kern_packet* lb;	
 }

```
#### if_ports_used_stats

```diff

 uint64_t ifpu_delayed_attributed_wake_event;	
 uint64_t ifpu_delayed_unattributed_wake_event;	
 uint64_t ifpu_delayed_wake_event_undelivered;	
+uint64_t ifpu_connection_idle_wake;	
+uint64_t ifpu_lpw_connection_idle_wake;	
+uint64_t ifpu_lpw_not_idle_wake;	
+uint64_t ifpu_lpw_to_full_wake;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.149

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.149 {
-struct netif_queue* ptr;	
-struct netif_queue* ub;	
-struct netif_queue* lb;	
+struct {
+ring_id_t ncre_ring_id;	
+uint32_t __ncre_align_reserved;	
+channel_ring_stats ncre_stats;	
+channel_ring_user_stats ncre_user_stats;	
+channel_ring_error_stats ncre_error_stats;	
+}
+* ptr;	
+struct {
+ring_id_t ncre_ring_id;	
+uint32_t __ncre_align_reserved;	
+channel_ring_stats ncre_stats;	
+channel_ring_user_stats ncre_user_stats;	
+channel_ring_error_stats ncre_error_stats;	
+}
+* ub;	
+struct {
+ring_id_t ncre_ring_id;	
+uint32_t __ncre_align_reserved;	
+channel_ring_stats ncre_stats;	
+channel_ring_user_stats ncre_user_stats;	
+channel_ring_error_stats ncre_error_stats;	
+}
+* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.174

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.174 {
-struct ucred* ptr;	
-struct ucred* ub;	
-struct ucred* lb;	
+struct nxprov_params* ptr;	
+struct nxprov_params* ub;	
+struct nxprov_params* lb;	
 }

```
#### nvme_ppl

```diff

 nvme_cid_mode_t fCIDState[257];	
 uint32_t fPersistentMappingsCount;	
 _Bool nvmeBARRegsWorkaround;	
+_Bool nvmeBARSecureRegLayout;	
 volatile uint32_t* nvmeBARSRegs;	
 uint32_t aqa;	
 uint64_t asqAddr;	

```
#### __bounds_safety::wide_ptr.bidi_indexable.126

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.126 {
-struct user64_timeval* ptr;	
-struct user64_timeval* ub;	
-struct user64_timeval* lb;	
+struct __packet_opt* ptr;	
+struct __packet_opt* ub;	
+struct __packet_opt* lb;	
 }

```
#### __bounds_safety::wide_ptr.indexable.48

```diff

 struct __bounds_safety::wide_ptr.indexable.48 {
-const void* ptr;	
-const void* ub;	
+void* ptr;	
+void* ub;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.78

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.78 {
-void* ptr;	
-void* ub;	
-void* lb;	
+struct netif_stats* ptr;	
+struct netif_stats* ub;	
+struct netif_stats* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.82

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.82 {
-struct __kern_buflet_ext* ptr;	
-struct __kern_buflet_ext* ub;	
-struct __kern_buflet_ext* lb;	
+struct kern_nexus* ptr;	
+struct kern_nexus* ub;	
+struct kern_nexus* lb;	
 }

```
#### IOService_CreatePMAssertion_Msg_Content

```c
struct IOService_CreatePMAssertion_Msg_Content {
  IORPCMessage __hdr;
  OSObjectRef  __object;
  uint32_t     assertionBits;
  bool         synced;
}

```
#### __bounds_safety::wide_ptr.indexable.44

```diff

 struct __bounds_safety::wide_ptr.indexable.44 {
-uint8_t* ptr;	
-uint8_t* ub;	
+u_int32_t* ptr;	
+u_int32_t* ub;	
 }

```
#### IOService_ReleasePMAssertion_Msg_Content

```c
struct IOService_ReleasePMAssertion_Msg_Content {
  IORPCMessage __hdr;
  OSObjectRef  __object;
  uint64_t     assertionID;
}

```
#### thread_ro

```diff

 struct proc* tro_proc;	
 struct proc_ro* tro_proc_ro;	
 struct task* tro_task;	
-struct ipc_port* tro_self_port;	
-struct ipc_port* tro_settable_self_port;	
 struct ipc_port* tro_ports[3];	
+struct ipc_port* tro_settable_self_port;	
 struct exception_action* tro_exc_actions;	
 }

```
#### net_aop_stats

```c
struct net_aop_stats {
  errno_t(void *, net_aop_stats_type_t, uint8_t *, size_t);
  *gs_stats;
  void *gs_prov_ctx;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.151

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.151 {
-struct netif_qset* ptr;	
-struct netif_qset* ub;	
-struct netif_qset* lb;	
+struct netif_qstats* ptr;	
+struct netif_qstats* ub;	
+struct netif_qstats* lb;	
 }

```
#### IOService_ReleasePMAssertion_Rpl_Content

```c
struct IOService_ReleasePMAssertion_Rpl_Content {
  IORPCMessage __hdr;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.9

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.9 {
-struct kern_nexus_provider* ptr;	
-struct kern_nexus_provider* ub;	
-struct kern_nexus_provider* lb;	
+void* ptr;	
+void* ub;	
+void* lb;	
 }

```
#### ip6_pktopts

```diff

 struct ip6_pktopts {
-struct mbuf* ip6po_m;	
-int ip6po_hlim;	
+int16_t ip6po_hlim;	
+int16_t ip6po_tclass;	
+int8_t ip6po_minmtu;	
+int8_t ip6po_prefer_tempaddr;	
+int8_t ip6po_flags;	
 struct in6_pktinfo* ip6po_pktinfo;	
 struct ip6po_nhinfo ip6po_nhinfo;	
 struct ip6_hbh* ip6po_hbh;	
 struct ip6_dest* ip6po_dest1;	
 struct ip6po_rhinfo ip6po_rhinfo;	
 struct ip6_dest* ip6po_dest2;	
-int ip6po_tclass;	
-int ip6po_minmtu;	
-int ip6po_prefer_tempaddr;	
-int ip6po_flags;	
 }

```
#### machine_thread

```diff

 arm_neon_saved_state_t* __ptrauth(DA, true, 0x356a) uNeon;	
 arm_saved_state_t* kpcb;	
 union {
-arm_state_hdr_t* umatrix_hdr;	
-arm_sme_saved_state_t* usme;	
-arm_amx_saved_state_t* uamx;	
+arm_state_hdr_t* __ptrauth(DA, true, 0x2f18) umatrix_hdr;	
+arm_sme_saved_state_t* __ptrauth(DA, true, 0x2f18) usme;	
+arm_amx_saved_state_t* __ptrauth(DA, true, 0x2f18) uamx;	
 }
  ;	
 long x86_64_compat;	

 uint64_t jop_pid;	
 uint64_t sprr_kern_perm;	
 uint64_t tpidr2_el0;	
+_Bool reserved15;	
 }

```
#### __bounds_safety::wide_ptr.indexable.125

```diff

 struct __bounds_safety::wide_ptr.indexable.125 {
-uint8_t* ptr;	
-uint8_t* ub;	
+char* ptr;	
+char* ub;	
 }

```
#### flowadv_fcentry

```diff

  fce_link;	
 u_int32_t fce_flowsrc_type;	
 u_int32_t fce_flowid;	
-u_int32_t fce_ce_cnt;	
+u_int32_t fce_congestion_cnt;	
+u_int32_t l4s_ce_cnt;	
 u_int32_t fce_pkts_since_last_report;	
 fce_event_type_t fce_event_type;	
 flowadv_token_t fce_flowsrc_token;	

```
#### __flowadv_entry

```diff

 uuid_t fae_id;	
 }
  ;	
-volatile uint32_t fae_ce_cnt;	
+volatile uint32_t fae_congestion_cnt;	
 volatile uint32_t fae_pkt_cnt;	
 volatile uint32_t fae_flags;	
 uint32_t fae_flowid;	

```
#### IOMemoryDescriptorReserved

```diff

 vm_tag_t kernelTag;	
 vm_tag_t userTag;	
 task_t creator;	
-class OSObject* contextObject;	
+OSPtr<OSDictionary> contextObjects;	
 }

```
#### ifreq

```diff

 struct if_interface_state ifru_interface_state;	
 u_int32_t ifru_probe_connectivity;	
 u_int32_t ifru_ecn_mode;	
+uint32_t ifru_l4s_mode;	
 u_int32_t ifru_qosmarking_mode;	
 u_int32_t ifru_qosmarking_enabled;	
 u_int32_t ifru_disable_output;	

 u_int8_t ifru_is_directlink;	
 u_int8_t ifru_is_vpn;	
 uint32_t ifru_delay_wake_pkt_event;	
+u_int8_t ifru_is_companionlink;	
 }
  ifr_ifru;	
 }

```
#### ifmediareq64

```c
struct ifmediareq64 {
  char          ifm_name[16];
  int           ifm_current;
  int           ifm_mask;
  int           ifm_status;
  int           ifm_active;
  int           ifm_count;
  user64_addr_t ifmu_ulist;
}

```
#### net_aop_provider_handle

```c
struct net_aop_provider_handle {
  struct net_aop_provider_init         kaop_ext;
  void                                *kaop_prov_ctx;
  struct net_aop_flow_setup            kaop_fsp;
  struct net_aop_flow_stats            kaop_fs;
  struct net_aop_stats                 kaop_gs;
  struct net_aop_proc_activity_bitmaps kaop_pb;
  uint32_t                             kaop_capabilities;
  uint32_t                             kaop_flags;
  os_refcnt_t                          kaop_refcnt;
}

```
#### vnop_verify_args

```diff

 void** a_verify_ctxp;	
 vnode_verify_flags_t a_flags;	
 vfs_context_t a_context;	
+vnode_verify_kind_t* a_verifykind;	
 }

```
#### nstat_client_details

```c
struct nstat_client_details {
  uint32_t nstat_client_id;
  pid_t    nstat_client_pid;
  uint32_t nstat_client_watching;
  uint32_t nstat_client_added_src;
}

```
#### __bounds_safety::wide_ptr.indexable.32

```c
struct __bounds_safety::wide_ptr.indexable.32 {
  char *ptr;
  char *ub;
}

```
#### firehose_buffer_header_s

```diff

 volatile uint16_t fbh_ring_mem_head;	
 volatile uint16_t fbh_ring_io_head;	
 struct firehose_buffer_bank_s fbh_bank;	
-struct firehose_buffer_stream_s fbh_stream[7];	
+struct firehose_buffer_stream_s fbh_stream[8];	
 uint64_t fbh_uniquepid;	
 pid_t fbh_pid;	
 mach_port_t fbh_logd_port;	

```
#### __bounds_safety::wide_ptr.bidi_indexable.13

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.13 {
-char* ptr;	
-char* ub;	
-char* lb;	
+struct nxctl_add_traffic_rule_inet_iocargs* ptr;	
+struct nxctl_add_traffic_rule_inet_iocargs* ub;	
+struct nxctl_add_traffic_rule_inet_iocargs* lb;	
 }

```
#### walkarg

```diff

 struct walkarg {
+int w_op;	
+int w_sub;	
 struct sysctl_req* w_req;	
 }

```
#### _ca_event_disallowed_sharing_data_buffers

```c
struct _ca_event_disallowed_sharing_data_buffers {
  ca_sstr proc_name[33];
  ca_sstr backtrace[340];
}

```
#### IOService_CreatePMAssertion_Rpl_Content

```c
struct IOService_CreatePMAssertion_Rpl_Content {
  IORPCMessage       __hdr;
  unsigned long long assertionID;
}

```
#### _vm_map

```diff

 unsigned int uses_user_ranges;	
 unsigned int tpro_enforcement;	
 unsigned int corpse_source;	
+unsigned int vmmap_sealed;	
 unsigned int res0;	
 unsigned int pad;	
 unsigned int timestamp;	

```
#### _ca_event_trap_telemetry_internal

```diff

 struct _ca_event_trap_telemetry_internal {
 ca_sstr backtrace[256];	
+ca_sstr kernel_platform[12];	
 unsigned long long trap_code;	
 unsigned long long trap_offset;	
 unsigned long long trap_type;	

```
#### ifcq_sysctl_oid

```c
struct ifcq_sysctl_oid {
  struct sysctl_oid_list ifcq_oid_list;
  struct sysctl_oid      ifcq_oid;
  char                   ifcq_name[32];
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.218

```c
struct __bounds_safety::wide_ptr.bidi_indexable.218 {
  struct _necp_arena_info_list *ptr;
  struct _necp_arena_info_list *ub;
  struct _necp_arena_info_list *lb;
}

```
#### vm_shared_region

```diff

 cpu_type_t sr_cpu_type;	
 cpu_subtype_t sr_cpu_subtype;	
 ipc_port_t sr_mem_entry;	
+vm_map_t sr_config_map;	
 mach_vm_offset_t sr_first_mapping;	
 mach_vm_offset_t sr_base_address;	
 mach_vm_size_t sr_size;	

```
#### __block_literal_36

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- void ();* __FuncPtr;	
-struct __block_descriptor_withcopydispose* __descriptor;	
-struct {
-void* __isa;	
-void* __forwarding;	
-int __flags;	
-int __size;	
-lck_rw_type_t lck_rw_type;	
-}
-* lck_rw_type;	
-lck_rw_t* lock;	
+ bool (const class OSSymbol*, class OSObject*);* __FuncPtr;	
+struct __block_descriptor* __descriptor;	
+class IOStateNotificationListener* listener;	
 }

```
#### _CEBuffer

```c
struct _CEBuffer {
  const uint8_t *data;
  size_t         length;
}

```
#### mac_policy_ops

```diff

 mpo_vnode_notify_swap_t* mpo_vnode_notify_swap;	
 mpo_vnode_notify_unlink_t* mpo_vnode_notify_unlink;	
 mpo_vnode_check_swap_t* mpo_vnode_check_swap;	
-mpo_reserved_hook_t* mpo_reserved33;	
-mpo_reserved_hook_t* mpo_reserved34;	
+mpo_vnode_check_dataprotect_set_t* mpo_vnode_check_dataprotect_set;	
+mpo_mount_check_remount_with_flags_t* mpo_mount_check_remount_with_flags;	
 mpo_mount_notify_mount_t* mpo_mount_notify_mount;	
 mpo_vnode_check_copyfile_t* mpo_vnode_check_copyfile;	
 mpo_mount_check_quotactl_t* mpo_mount_check_quotactl;	

 mpo_proc_check_sched_t* mpo_proc_check_sched;	
 mpo_proc_check_setaudit_t* mpo_proc_check_setaudit;	
 mpo_proc_check_setauid_t* mpo_proc_check_setauid;	
-mpo_reserved_hook_t* mpo_reserved64;	
+mpo_proc_check_iopolicysys_t* mpo_proc_check_iopolicysys;	
 mpo_proc_check_signal_t* mpo_proc_check_signal;	
 mpo_proc_check_wait_t* mpo_proc_check_wait;	
 mpo_proc_check_dump_core_t* mpo_proc_check_dump_core;	

```
#### vm_pageout_stat

```diff

 unsigned long vm_page_pageable_internal_count;	
 unsigned long vm_page_pageable_external_count;	
 unsigned long vm_page_xpmapped_external_count;	
+unsigned long vm_page_swapped_count;	
+uint64_t swapouts;	
+uint64_t swapins;	
 unsigned int pages_grabbed;	
 unsigned int pages_freed;	
 unsigned int pages_compressed;	

```
#### _ca_event_reply_port_semantics_violations

```diff

 ca_sstr team_id[32];	
 ca_sstr signing_id[128];	
 unsigned long long reply_port_semantics_violation;	
+unsigned long long msgh_id;	
 }

```
#### fcl_stat

```diff

 uint64_t fcl_ignore_tx_time;	
 uint64_t fcl_paced_pkts;	
 uint64_t fcl_fcl_pacemaker_needed;	
+uint64_t fcl_high_delay_drop;	
+uint64_t fcl_congestion_feedback;	
 }

```
#### tcp_info

```diff

 uint64_t tcpi_delivered_ce_bytes;	
 uint64_t tcpi_flow_control_total_time;	
 uint64_t tcpi_rcvwnd_limited_total_time;	
+uint64_t tcpi_pacing_rate;	
+uint64_t tcpi_max_pacing_rate;	
 }

```
#### __bounds_safety::wide_ptr.indexable.105

```diff

 struct __bounds_safety::wide_ptr.indexable.105 {
-void* ptr;	
-void* ub;	
+struct icmp6_nodeinfo* ptr;	
+struct icmp6_nodeinfo* ub;	
 }

```
#### codel_status

```c
struct codel_status {
  boolean_t dropping;
  uint32_t  lastcnt;
  uint32_t  count;
  uint64_t  first_above_time;
  uint64_t  drop_next;
}

```
#### static_if_key

```diff

 struct static_if_key {
-short sik_enable_count;	
-short sik_init_value;	
-unsigned int sik_entries_count;	
+int16_t sik_enable_count;	
+bool sik_init_value;	
+bool sik_modified;	
+uint32_t sik_entries_count;	
 static_if_entry_t sik_entries_head;	
+struct static_if_key* sik_modified_next;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.95

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.95 {
-struct nx_netif* ptr;	
-struct nx_netif* ub;	
-struct nx_netif* lb;	
+struct mbuf* ptr;	
+struct mbuf* ub;	
+struct mbuf* lb;	
 }

```
#### __block_literal_17

```diff

 void* __forwarding;	
 int __flags;	
 int __size;	
-bool allPowerStates;	
+bool addClass;	
 }
-* allPowerStates;	
+* addClass;	
+class OSDictionary* retProps;	
+class OSDictionary* props;	
 }

```
#### page_table_attr

```diff

 const uint64_t pta_page_size;	
 const uint64_t pta_page_shift;	
 const uint8_t geometry_id;	
+const uint64_t pta_va_valid_mask;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.111

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.111 {
-struct kern_pbufpool* ptr;	
-struct kern_pbufpool* ub;	
-struct kern_pbufpool* lb;	
+struct __kern_quantum* ptr;	
+struct __kern_quantum* ub;	
+struct __kern_quantum* lb;	
 }

```
#### __block_literal_21

```diff

 int __flags;	
 int __reserved;	
  bool (class OSObject*);* __FuncPtr;	
-struct __block_descriptor_withcopydispose* __descriptor;	
-struct {
-void* __isa;	
-void* __forwarding;	
-int __flags;	
-int __size;	
-bool allPowerStates;	
-}
-* allPowerStates;	
+struct __block_descriptor* __descriptor;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.198

```c
struct __bounds_safety::wide_ptr.bidi_indexable.198 {
  struct necp_stat_counts *ptr;
  struct necp_stat_counts *ub;
  struct necp_stat_counts *lb;
}

```
#### pktsched_ops

```c
struct pktsched_ops {
  uint8_t ps_id;
  uint8_t ps_ops_flags;
  int(struct ifclassq *, u_int32_t, classq_pkt_type_t);
  *ps_setup;
  void(struct ifclassq *);
  *ps_teardown;
  int(struct ifclassq *, classq_pkt_t *, classq_pkt_t *, uint32_t, uint32_t,
      boolean_t *);
  *ps_enq;
  int(struct ifclassq *, u_int32_t, u_int32_t, classq_pkt_t *, classq_pkt_t *,
      u_int32_t *, u_int32_t *, uint8_t);
  *ps_deq;
  int(struct ifclassq *, mbuf_svc_class_t, u_int32_t, u_int32_t, classq_pkt_t *,
      classq_pkt_t *, u_int32_t *, u_int32_t *, uint8_t);
  *ps_deq_sc;
  int(struct ifclassq *,
      enum cqrq{CLASSQRQ_PURGE = 1, CLASSQRQ_PURGE_SC = 2, CLASSQRQ_EVENT = 3,
                CLASSQRQ_THROTTLE = 4, CLASSQRQ_STAT_SC = 5},
      void *);
  *ps_req;
  int(struct ifclassq *, uint8_t, u_int32_t, struct if_ifclassq_stats *);
  *ps_stats;
  boolean_t(struct ifclassq *);
  *ps_allow_dequeue;
  struct {
    struct pktsched_ops  *le_next;
    struct pktsched_ops **le_prev;
  } ps_ops_link;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.96

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.96 {
-struct kern_nexus* ptr;	
-struct kern_nexus* ub;	
-struct kern_nexus* lb;	
+struct {
+struct __kern_buflet_ext* slh_first;	
+}
+* ptr;	
+struct {
+struct __kern_buflet_ext* slh_first;	
+}
+* ub;	
+struct {
+struct __kern_buflet_ext* slh_first;	
+}
+* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.172

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.172 {
-struct necp_client_browse_result* ptr;	
-struct necp_client_browse_result* ub;	
-struct necp_client_browse_result* lb;	
+struct tseg_qent* ptr;	
+struct tseg_qent* ub;	
+struct tseg_qent* lb;	
 }

```
#### aop_ip6_stats

```c
struct aop_ip6_stats {
  uint64_t _arr[19];
}

```
#### tcp_heuristic

```diff

 uint8_t th_tfo_req_rst;	
 uint8_t th_mptcp_loss;	
 uint8_t th_mptcp_success;	
-uint8_t th_ecn_loss;	
-uint8_t th_ecn_aggressive;	
 uint8_t th_ecn_droprst;	
-uint8_t th_ecn_droprxmt;	
 uint8_t th_ecn_synrst;	
 uint32_t th_tfo_enabled_time;	
 uint32_t th_tfo_backoff_until;	

```
#### IOCircularDataQueueDescription

```c
struct IOCircularDataQueueDescription {
  uint64_t sentinel;
  uint32_t allocMemSize;
  uint32_t entryDataSize;
  uint32_t memorySize;
  uint32_t numEntries;
  uint32_t dataSize;
  uint32_t padding;
}

```
#### _CEData

```c
struct _CEData {
  const uint8_t *data;
  size_t         length;
}

```
#### __bounds_safety::wide_ptr.indexable.106

```c
struct __bounds_safety::wide_ptr.indexable.106 {
  void *ptr;
  void *ub;
}

```
#### net_aop_proc_activity_bitmaps

```c
struct net_aop_proc_activity_bitmaps {
  errno_t(void *, struct aop_proc_activity_bitmap *, uint16_t *);
  *pab_activity_bitmap;
  void *pab_prov_ctx;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.19

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.19 {
-struct skmem_region* ptr;	
-struct skmem_region* ub;	
-struct skmem_region* lb;	
+struct nxctl_add_traffic_rule_eth_iocargs* ptr;	
+struct nxctl_add_traffic_rule_eth_iocargs* ub;	
+struct nxctl_add_traffic_rule_eth_iocargs* lb;	
 }

```
#### task_effective_policy

```diff

 uint64_t tep_live_donor;	
 uint64_t tep_qos_clamp;	
 uint64_t tep_qos_ceiling;	
-uint64_t tep_adaptive_bg;	
+uint64_t tep_promote_above_task;	
 uint64_t tep_coalition_bg;	
+uint64_t tep_runaway_mitigation;	
 uint64_t tep_reserved;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.209

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.209 {
-struct necp_client_observer_update* ptr;	
-struct necp_client_observer_update* ub;	
-struct necp_client_observer_update* lb;	
+struct sockaddr_dl* ptr;	
+struct sockaddr_dl* ub;	
+struct sockaddr_dl* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.173

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.173 {
-struct kern_nexus_provider* ptr;	
-struct kern_nexus_provider* ub;	
-struct kern_nexus_provider* lb;	
+struct sockaddr_in* ptr;	
+struct sockaddr_in* ub;	
+struct sockaddr_in* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.50

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.50 {
-struct nexus_adapter* ptr;	
-struct nexus_adapter* ub;	
-struct nexus_adapter* lb;	
+struct nxbind* ptr;	
+struct nxbind* ub;	
+struct nxbind* lb;	
 }

```
#### nxctl_traffic_rule_type

```diff

 nxctl_traffic_rule_create_cb_t* ntrt_create;	
 nxctl_traffic_rule_destroy_cb_t* ntrt_destroy;	
 nxctl_traffic_rule_get_all_cb_t* ntrt_get_all;	
-struct nxctl_traffic_rule_inet_storage* ntrt_storage;	
+nxctl_traffic_rule_get_count_cb_t* ntrt_get_count;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.28

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.28 {
-struct __kern_packet* ptr;	
-struct __kern_packet* ub;	
-struct __kern_packet* lb;	
+struct netif_stats* ptr;	
+struct netif_stats* ub;	
+struct netif_stats* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.235

```c
struct __bounds_safety::wide_ptr.bidi_indexable.235 {
  struct necp_drop_dest_entry *ptr;
  struct necp_drop_dest_entry *ub;
  struct necp_drop_dest_entry *lb;
}

```
#### user32_flocktimeout

```c
struct user32_flocktimeout {
  struct flock           fl;
  struct user32_timespec timeout;
}

```
#### rsb_entry

```diff

 struct rsb_entry {
 match_record_s record;	
+trap_telemetry_extra_data_u extra_data;	
 trap_telemetry_options_s options;	
 size_t bt_frames_count;	
 uintptr_t bt_frames[15];	

```
#### aop_tcp_stats

```c
struct aop_tcp_stats {
  uint64_t _arr[76];
}

```
#### psemcache

```diff

  psem_hash;	
 struct pseminfo* pseminfo;	
 size_t psem_nlen;	
+size_t psem_teamidlen;	
 char psem_name[32];	
+char psem_teamid[32];	
 }

```
#### aop_ip_stats

```c
struct aop_ip_stats {
  uint64_t _arr[22];
}

```
#### rn_base_entry

```c
struct rn_base_entry {
  union {
    struct {
      struct radix_node tt;
      struct radix_node t;
    } _split_nodes;
    struct radix_node rnb_nodes[2];
  };
}

```
#### nstat_extended_sock_locus

```c
struct nstat_extended_sock_locus {
  nstat_sock_locus nesl_sock_locus;
  union {
    struct sockaddr_in  v4;
    struct sockaddr_in6 v6;
  } nesl_local;
  union {
    struct sockaddr_in  v4;
    struct sockaddr_in6 v6;
  } nesl_remote;
  _Bool        nesl_cached;
  unsigned int nesl_if_index;
}

```
#### __bounds_safety::wide_ptr.indexable.75

```diff

 struct __bounds_safety::wide_ptr.indexable.75 {
-void* ptr;	
-void* ub;	
+const bitmap_t* ptr;	
+const bitmap_t* ub;	
 }

```
#### xnu_hw_shmem_dbg_command_info

```diff

 struct xnu_hw_shmem_dbg_command_info {
-volatile uint32_t xhsdci_status;	
+volatile xhsdci_status_t xhsdci_status;	
 uint32_t xhsdci_seq_no;	
 volatile uint64_t xhsdci_buf_phys_addr;	
 volatile uint32_t xhsdci_buf_data_length;	
 uint64_t xhsdci_coredump_total_size_uncomp;	
 uint64_t xhsdci_coredump_total_size_sent_uncomp;	
 uint32_t xhsdci_page_size;	
+char xhsdci_file_name[64];	
+xhsdci_file_flags_t xhsdci_file_flags;	
 }

```
#### nstat_locus

```c
struct nstat_locus {
  tailq_head_nstat_src ntl_src_queue;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.135

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.135 {
-const struct flow_key* ptr;	
-const struct flow_key* ub;	
-const struct flow_key* lb;	
+struct sk_stats_flow_route* ptr;	
+struct sk_stats_flow_route* ub;	
+struct sk_stats_flow_route* lb;	
 }

```
#### necp_client_flow

```diff

 unsigned int assigned;	
 unsigned int has_protoctl_event;	
 unsigned int check_tcp_heuristics;	
-unsigned int _reserved;	
+unsigned int aop_offload;	
+unsigned int aop_stat_index_valid;	
 union {
 uuid_t nexus_agent;	
 struct {

 struct necp_client_flow_protoctl_event protoctl_event;	
 union necp_sockaddr_union local_addr;	
 union necp_sockaddr_union remote_addr;	
+uint32_t flow_tag;	
+uint32_t stats_index;	
 size_t assigned_results_length;	
 __bounds_safety::counted_by::assigned_results_length assigned_results;	
 }

```
#### proc_ident

```diff

 struct proc_ident {
 uint64_t p_uniqueid;	
+pid_t may_exit;	
+pid_t may_exec;	
+pid_t reserved;	
 pid_t p_pid;	
 int p_idversion;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.32

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.32 {
-uint8_t* ptr;	
-uint8_t* ub;	
-uint8_t* lb;	
+struct kern_pbufpool* ptr;	
+struct kern_pbufpool* ub;	
+struct kern_pbufpool* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.21

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.21 {
-struct m_tag* ptr;	
-struct m_tag* ub;	
-struct m_tag* lb;	
+struct kalloc_type_view* ptr;	
+struct kalloc_type_view* ub;	
+struct kalloc_type_view* lb;	
 }

```
#### task_memorystatus_snapshot

```c
struct task_memorystatus_snapshot {
  int32_t tms_current_memlimit;
  int32_t tms_effectivepriority;
  int32_t tms_requestedpriority;
  int32_t tms_assertionpriority;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.116

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.116 {
-struct flow_route* ptr;	
-struct flow_route* ub;	
-struct flow_route* lb;	
+struct ifnet* ptr;	
+struct ifnet* ub;	
+struct ifnet* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.107

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.107 {
-struct mbuf* ptr;	
-struct mbuf* ub;	
-struct mbuf* lb;	
+struct ifnet* ptr;	
+struct ifnet* ub;	
+struct ifnet* lb;	
 }

```
#### ledger_entry_counter

```c
struct ledger_entry_counter {
  volatile uint32_t lec_flags;
  counter_t         lec_counter;
}

```
#### memory_entry_subsystem

```diff

 mach_msg_id_t end;	
 unsigned int maxsize;	
 vm_address_t reserved;	
-struct kern_routine_descriptor kroutine[3];	
+struct kern_routine_descriptor kroutine[4];	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.41

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.41 {
-struct skmem_obj* ptr;	
-struct skmem_obj* ub;	
-struct skmem_obj* lb;	
+struct kern_pbufpool_u_bkt* ptr;	
+struct kern_pbufpool_u_bkt* ub;	
+struct kern_pbufpool_u_bkt* lb;	
 }

```
#### __block_literal_16

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- bool (class OSObject*);* __FuncPtr;	
+ IOReturn ();* __FuncPtr;	
 struct __block_descriptor_withcopydispose* __descriptor;	
 struct {
 void* __isa;	
 void* __forwarding;	
 int __flags;	
 int __size;	
-bool addClass;	
+class OSObject* object;	
 }
-* addClass;	
-class OSDictionary* retProps;	
-class OSDictionary* props;	
+* object;	
+class IOService* provider;	
+const char* name;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.7

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.7 {
-struct skmem_magtype* ptr;	
-struct skmem_magtype* ub;	
-struct skmem_magtype* lb;	
+const char* ptr;	
+const char* ub;	
+const char* lb;	
 }

```
#### __bounds_safety::wide_ptr.indexable.134

```c
struct __bounds_safety::wide_ptr.indexable.134 {
  void *ptr;
  void *ub;
}

```
#### __bounds_safety::wide_ptr.indexable.76

```diff

 struct __bounds_safety::wide_ptr.indexable.76 {
-const bitmap_t* ptr;	
-const bitmap_t* ub;	
+void* ptr;	
+void* ub;	
 }

```
#### shmem_stage_data

```diff

 struct shmem_stage_data {
+_Bool signal_done;	
 uint32_t seq_no;	
 uint64_t contact_deadline;	
 uint64_t contact_deadline_interval;	

```
#### kern_timeout

```c
struct kern_timeout {
  uint64_t  start_mt;
  uint64_t  end_mt;
  uint64_t  int_mt;
  uint64_t  start_cycles;
  uint64_t  int_cycles;
  uint64_t  start_instrs;
  uint64_t  int_instrs;
  uintptr_t bt[3];
}

```
#### kdp_output_stage_funcs

```diff

 struct kdp_output_stage_funcs {
- void (struct kdp_output_stage*);* kosf_reset;	
+ kern_return_t (struct kdp_output_stage*, const char*, kern_coredump_type_t);* kosf_reset;	
  kern_return_t (struct kdp_output_stage*, unsigned int, char*, uint64_t, void*);* kosf_outproc;	
  void (struct kdp_output_stage*);* kosf_free;	
 }

```
#### IODataQueueInternal

```c
struct IODataQueueInternal {
  mach_msg_header_t msg;
  UInt32            queueSize;
}

```
#### nstat_src

```diff

 struct nstat_src {
 tailq_entry_nstat_src nts_client_link;	
+tailq_entry_nstat_src nts_locus_link;	
+nstat_locus* nts_locus;	
 nstat_client* nts_client;	
 nstat_src_ref_t nts_srcref;	
 nstat_provider* nts_provider;	

```
#### __bounds_safety::wide_ptr.bidi_indexable.113

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.113 {
-struct ifnet* ptr;	
-struct ifnet* ub;	
-struct ifnet* lb;	
+struct kern_pbufpool* ptr;	
+struct kern_pbufpool* ub;	
+struct kern_pbufpool* lb;	
 }

```
#### jetsam_snapshot_entry

```diff

 uint64_t csflags;	
 uint32_t cs_trust_level;	
 uint64_t jse_neural_nofootprint_total_pages;	
+uint64_t jse_prio_start;	
 }

```
#### pgo_iothread_state

```diff

 struct pgo_iothread_state {
 struct vm_pageout_queue* q;	
 void* current_early_swapout_chead;	
-void* current_regular_swapout_chead;	
+void* current_regular_swapout_cheads[16];	
 void* current_late_swapout_chead;	
 char* scratch_buf;	
 int id;	

```
#### __bounds_safety::wide_ptr.bidi_indexable.42

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.42 {
-uint64_t* ptr;	
-uint64_t* ub;	
-uint64_t* lb;	
+struct m_tag* ptr;	
+struct m_tag* ub;	
+struct m_tag* lb;	
 }

```
#### __bounds_safety::wide_ptr.indexable.149

```c
struct __bounds_safety::wide_ptr.indexable.149 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### hv_mem_notify_t

```c
struct hv_mem_notify_t {
  vm_map_t    map;
  uint64_t    context;
  uint64_t    base_ipa;
  uint64_t    end_ipa;
  mach_port_t port;
  struct {
    struct hv_mem_notify_t *rbe_left;
    struct hv_mem_notify_t *rbe_right;
    struct hv_mem_notify_t *rbe_parent;
  } link;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.216

```c
struct __bounds_safety::wide_ptr.bidi_indexable.216 {
  nstat_msg_src_added *ptr;
  nstat_msg_src_added *ub;
  nstat_msg_src_added *lb;
}

```
#### syncookie_secret

```c
struct syncookie_secret {
  volatile u_int oddeven;
  uint8_t[16] key[2];
  uint32_t last_updated;
}

```
#### __bounds_safety::wide_ptr.indexable.127

```c
struct __bounds_safety::wide_ptr.indexable.127 {
  char *ptr;
  char *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.127

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.127 {
-struct m_tag* ptr;	
-struct m_tag* ub;	
-struct m_tag* lb;	
+struct inpcb** ptr;	
+struct inpcb** ub;	
+struct inpcb** lb;	
 }

```
#### hv_mem_notify_tree_s

```c
struct hv_mem_notify_tree_s {
  struct hv_mem_notify_t *rbh_root;
}

```
#### hv_vm_t

```diff

 os_refcnt_t refcnt;	
 hv_vm_isa_t isa;	
 uint64_t oem_hc;	
+hv_mem_notify_tree_t mem_notify_tree;	
+uint8_t mem_notify_count;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.201

```c
struct __bounds_safety::wide_ptr.bidi_indexable.201 {
  struct if_proto **ptr;
  struct if_proto **ub;
  struct if_proto **lb;
}

```
#### inpcb

```diff

 uint64_t inp_fadv_total_time;	
 uint64_t inp_fadv_start_time;	
 uint64_t inp_fadv_cnt;	
-char* inp_saved_ppcb;	
 struct inpcbpolicy* inp_sp;	
 struct inp_necp_attributes inp_necp_attributes;	
 struct necp_inpcb_result inp_policyresult;	

 uint8_t inp_keepalive_datalen;	
 uint8_t inp_keepalive_type;	
 uint16_t inp_keepalive_interval;	
-uint32_t inp_nstat_refcnt;	
-struct inp_stat* inp_stat;	
-struct inp_stat* inp_cstat;	
-struct inp_stat* inp_wstat;	
-struct inp_stat* inp_Wstat;	
-struct inp_stat* inp_btstat;	
-uint8_t inp_stat_store[40];	
-uint8_t inp_cstat_store[40];	
-uint8_t inp_wstat_store[40];	
-uint8_t inp_Wstat_store[40];	
-uint8_t inp_btstat_store[40];	
-activity_bitmap_t inp_nw_activity;	
+struct nstat_sock_locus* inp_nstat_locus;	
+struct media_stats inp_mstat;	
 uint64_t inp_start_timestamp;	
 uint64_t inp_connect_timestamp;	
 char inp_last_proc_name[17];	
 char inp_e_proc_name[17];	
+uint64_t inp_max_pacing_rate;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.204

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.204 {
-struct ifaddr* ptr;	
-struct ifaddr* ub;	
-struct ifaddr* lb;	
+struct skmem_cache* ptr;	
+struct skmem_cache* ub;	
+struct skmem_cache* lb;	
 }

```
#### net_aop_protocol_stats

```c
struct net_aop_protocol_stats {
  struct aop_ip_stats  aop_ip;
  struct aop_ip6_stats aop_ip6;
  struct aop_tcp_stats aop_tcp;
  struct aop_udp_stats aop_udp;
}

```
#### flow_entry

```diff

 struct flow_entry** tqe_prev;	
 }
  fe_rx_link;	
- void (struct nx_flowswitch*, struct flow_entry*, struct pktq*, uint32_t, uint32_t);* fe_rx_process;	
+ void (struct nx_flowswitch*, struct flow_entry*, struct pktq*, uint32_t, struct mbufq*, uint32_t);* fe_rx_process;	
 uint64_t fe_rx_worker_tid;	
 uint32_t fe_rx_largest_size;	
 _Bool fe_tx_is_cont_frag;	

```
#### __bounds_safety::wide_ptr.indexable.103

```diff

 struct __bounds_safety::wide_ptr.indexable.103 {
-uint8_t* ptr;	
-uint8_t* ub;	
+uint64_t* ptr;	
+uint64_t* ub;	
 }

```
#### __bounds_safety::wide_ptr.indexable.43

```c
struct __bounds_safety::wide_ptr.indexable.43 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.145

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.145 {
-struct netif_llink* ptr;	
-struct netif_llink* ub;	
-struct netif_llink* lb;	
+struct __kern_quantum* ptr;	
+struct __kern_quantum* ub;	
+struct __kern_quantum* lb;	
 }

```
#### __kern_channel_ring

```diff

 struct __kern_channel_ring* ckr_pipe;	
 struct __user_channel_ring* ckr_save_ring;	
 lck_mtx_t ckr_qlock;	
-struct __kern_channel_ring** ckr_monitors;	
-uint32_t ckr_max_monitors;	
-uint32_t ckr_n_monitors;	
- int (struct __kern_channel_ring*, struct proc*, uint32_t);* ckr_mon_sync;	
- int (struct __kern_channel_ring*, struct proc*, uint32_t);* ckr_mon_notify;	
-uint32_t ckr_mon_tail;	
-uint32_t ckr_mon_pos;	
 uint32_t ckr_users;	
 int64_t ckr_tbr_token;	
 int64_t ckr_tbr_depth;	

```
#### __bounds_safety::wide_ptr.bidi_indexable.66

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.66 {
-struct kern_nexus_netif_llink_qset_init* ptr;	
-struct kern_nexus_netif_llink_qset_init* ub;	
-struct kern_nexus_netif_llink_qset_init* lb;	
+struct nxdom* ptr;	
+struct nxdom* ub;	
+struct nxdom* lb;	
 }

```
#### ccdigest_info

```diff

  void (ccdigest_state_t, size_t, const void*);* __ptrauth(IA, true, 0xc7a0) compress;	
  void (const struct ccdigest_info*, ccdigest_ctx_t, unsigned char*);* __ptrauth(IA, true, 0x1bda) final;	
 cc_impl_t impl;	
+ void (ccdigest_state_t, size_t, const void*, ccdigest_state_t, size_t, const void*);* __ptrauth(IA, true, 0xd5aa) compress_parallel;	
 }

```
#### __bounds_safety::wide_ptr.indexable.189

```c
struct __bounds_safety::wide_ptr.indexable.189 {
  struct nstat_msg_src_details *ptr;
  struct nstat_msg_src_details *ub;
}

```
#### aio_workq_usec_var

```c
struct aio_workq_usec_var {
  uint32_t usecs;
  uint64_t abstime;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.170

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.170 {
-necp_application_id_t* ptr;	
-necp_application_id_t* ub;	
-necp_application_id_t* lb;	
+symptoms_advisory_t* ptr;	
+symptoms_advisory_t* ub;	
+symptoms_advisory_t* lb;	
 }

```
#### _CEValueTypePair

```c
struct _CEValueTypePair {
  CEType_t    derType;
  CEElement_t derValue;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.178

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.178 {
-struct ether_header* ptr;	
-struct ether_header* ub;	
-struct ether_header* lb;	
+struct if_cellular_status_v1* ptr;	
+struct if_cellular_status_v1* ub;	
+struct if_cellular_status_v1* lb;	
 }

```
#### user64_package_ext_info

```c
struct user64_package_ext_info {
  user64_addr_t strings;
  uint32_t      num_entries;
  uint32_t      max_width;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.43

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.43 {
-struct __kern_channel_ring* ptr;	
-struct __kern_channel_ring* ub;	
-struct __kern_channel_ring* lb;	
+struct __kern_quantum* ptr;	
+struct __kern_quantum* ub;	
+struct __kern_quantum* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.222

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.222 {
-nstat_connection_descriptor* ptr;	
-nstat_connection_descriptor* ub;	
-nstat_connection_descriptor* lb;	
+struct necp_domain_trie_request* ptr;	
+struct necp_domain_trie_request* ub;	
+struct necp_domain_trie_request* lb;	
 }

```
#### nstat_global_counts

```diff

 struct nstat_global_counts {
+uint64_t nstat_global_count_version;	
+uint64_t nstat_global_exclusive_lock_uncontended;	
+uint64_t nstat_global_exclusive_lock_contended;	
+uint64_t nstat_global_shared_lock_uncontended;	
+uint64_t nstat_global_shared_lock_contended;	
 uint64_t nstat_global_client_current;	
 uint64_t nstat_global_client_max;	
 uint64_t nstat_global_client_allocs;	
+uint64_t nstat_global_client_alloc_fails;	
 uint64_t nstat_global_src_current;	
 uint64_t nstat_global_src_max;	
 uint64_t nstat_global_src_allocs;	
-uint64_t nstat_global_src_idlecheck_gone;	
-uint64_t nstat_global_tucookie_current;	
-uint64_t nstat_global_tucookie_max;	
-uint64_t nstat_global_tucookie_allocs;	
-uint64_t nstat_global_tucookie_skip_dead;	
-uint64_t nstat_global_tucookie_skip_stopusing;	
-uint64_t nstat_global_tucookie_alloc_fail;	
+uint64_t nstat_global_src_alloc_fails;	
+uint64_t nstat_global_tcp_sck_locus_current;	
+uint64_t nstat_global_tcp_sck_locus_max;	
+uint64_t nstat_global_tcp_sck_locus_allocs;	
+uint64_t nstat_global_tcp_sck_locus_alloc_fails;	
+uint64_t nstat_global_udp_sck_locus_current;	
+uint64_t nstat_global_udp_sck_locus_max;	
+uint64_t nstat_global_udp_sck_locus_allocs;	
+uint64_t nstat_global_udp_sck_locus_alloc_fails;	
 uint64_t nstat_global_tu_shad_current;	
 uint64_t nstat_global_tu_shad_max;	
 uint64_t nstat_global_tu_shad_allocs;	

 uint64_t nstat_global_procdetails_current;	
 uint64_t nstat_global_procdetails_max;	
 uint64_t nstat_global_procdetails_allocs;	
+uint64_t nstat_global_idlecheck_tcp_gone;	
+uint64_t nstat_global_idlecheck_udp_gone;	
+uint64_t nstat_global_idlecheck_route_src_gone;	
+uint64_t nstat_global_tcp_sck_locus_stop_using;	
+uint64_t nstat_global_udp_sck_locus_stop_using;	
+uint64_t nstat_global_pcb_detach_with_locus;	
+uint64_t nstat_global_pcb_detach_with_src;	
+uint64_t nstat_global_pcb_detach_without_locus;	
+uint64_t nstat_global_pcb_detach_udp;	
+uint64_t nstat_global_pcb_detach_tcp;	
+uint64_t nstat_global_sck_update_last_owner;	
+uint64_t nstat_global_sck_fail_first_owner;	
+uint64_t nstat_global_sck_fail_last_owner;	
+uint64_t nstat_global_tcp_desc_new_name;	
+uint64_t nstat_global_tcp_desc_fail_name;	
+uint64_t nstat_global_udp_desc_new_name;	
+uint64_t nstat_global_udp_desc_fail_name;	
+uint64_t nstat_global_tucookie_current;	
+uint64_t nstat_global_tucookie_max;	
+uint64_t nstat_global_tucookie_allocs;	
+uint64_t nstat_global_tucookie_alloc_fail;	
+uint64_t nstat_global_tucookie_skip_dead;	
+uint64_t nstat_global_tucookie_skip_stopusing;	
+uint64_t nstat_global_src_idlecheck_gone;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.74

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.74 {
-struct __user_slot_desc* ptr;	
-struct __user_slot_desc* ub;	
-struct __user_slot_desc* lb;	
+struct __kern_slot_desc* ptr;	
+struct __kern_slot_desc* ub;	
+struct __kern_slot_desc* lb;	
 }

```
#### aop_proc_activity_bitmap

```c
struct aop_proc_activity_bitmap {
  char                       proc_bundle_id[256];
  struct aop_activity_bitmap wifi_bitmap;
  struct aop_activity_bitmap cell_bitmap;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.210

```c
struct __bounds_safety::wide_ptr.bidi_indexable.210 {
  struct necp_client_result_netagent *ptr;
  struct necp_client_result_netagent *ub;
  struct necp_client_result_netagent *lb;
}

```
#### vm_page_free_queue

```c
struct vm_page_free_queue {
  struct vm_page_queue_free_head vmpfq_queues[128];
  uint32_t                       vmpfq_count;
}

```
#### tcp_inp

```c
struct tcp_inp {
  struct socket                      *so;
  struct inpcb                      **inp;
  struct tcpcb                      **tp;
  struct mbuf                        *m;
  struct tcphdr                      *th;
  struct tcpopt                      *to;
  __bounds_safety::counted_by::optlen optp;
  struct ip6_hdr                     *ip6;
  struct ip                          *ip;
  struct ifnet                       *ifp;
  struct proc                        *kernel_proc;
  tcp_seq                             iss;
  tcp_seq                             irs;
  uint32_t                            tiwin;
  uint32_t                            ts_offset;
  int                                 optlen;
  unsigned int                        ifscope;
  uint16_t                            peer_mss;
  uint8_t                             peer_wscale;
  _Bool                               sackok;
  _Bool                               ecnok;
  uint8_t                             ip_ecn;
  _Bool                               isipv6;
}

```
#### net_aop_capab_flow_setup

```c
struct net_aop_capab_flow_setup {
  uint32_t kaopcfsp_version;
  void    *kaopcfsp_prov_ctx;
  errno_t(void *, uint32_t, _Bool, uint32_t *);
  *kaopcfsp_config;
}

```
#### pmap_cpu_data

```diff

 _Atomic const volatile struct pmap* active_stage2_pmap;	
 unsigned int cpu_number;	
 _Bool copywindow_strong_sync[4];	
-_Bool inflight_disconnect;	
 pv_free_list_t pv_free;	
 pv_entry_t* pv_free_spill_marker;	
 }

```
#### counted_mbufq

```c
struct counted_mbufq {
  struct mbuf  *mq_first;
  struct mbuf **mq_last;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.81

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.81 {
-struct ether_vlan_header* ptr;	
-struct ether_vlan_header* ub;	
-struct ether_vlan_header* lb;	
+struct __kern_quantum* ptr;	
+struct __kern_quantum* ub;	
+struct __kern_quantum* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.184

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.184 {
-struct __kern_netif_intf_advisory* ptr;	
-struct __kern_netif_intf_advisory* ub;	
-struct __kern_netif_intf_advisory* lb;	
+struct tsegqe_head* ptr;	
+struct tsegqe_head* ub;	
+struct tsegqe_head* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.58

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.58 {
-struct kern_nexus_domain_provider* ptr;	
-struct kern_nexus_domain_provider* ub;	
-struct kern_nexus_domain_provider* lb;	
+struct __kern_packet** ptr;	
+struct __kern_packet** ub;	
+struct __kern_packet** lb;	
 }

```
#### ifclassq

```diff

 u_int32_t ifcq_target_qdelay;	
 u_int32_t ifcq_bytes;	
 u_int32_t ifcq_pkt_drop_limit;	
-uint64_t ifcq_doorbells;	
 void* ifcq_disc;	
+struct pktsched_ops* ifcq_ops;	
 struct ifclassq_disc_slot ifcq_disc_slots[10];	
 struct tb_regulator ifcq_tbr;	
+ifcq_oid_t ifcq_oid;	
 }

```
#### funmount_args

```c
struct funmount_args {
  char fd_l_[0];
  int  fd;
  char fd_r_[4];
  char flags_l_[0];
  int  flags;
  char flags_r_[4];
}

```
#### nstat_provider

```diff

  errno_t (__bounds_safety::sized_by::length, u_int32_t, void**);* nstat_lookup;	
  int (void*);* nstat_gone;	
  errno_t (void*, struct nstat_counts*, int*);* nstat_counts;	
+ errno_t (void*, struct nstat_detailed_counts*, int*);* nstat_details;	
  errno_t (nstat_client*, nstat_msg_add_all_srcs*);* nstat_watcher_add;	
  void (nstat_client*);* nstat_watcher_remove;	
  errno_t (void*, __bounds_safety::sized_by::len, size_t);* nstat_copy_descriptor;	
- void (void*, boolean_t);* nstat_release;	
+ void (void*);* nstat_release;	
  _Bool (void*, nstat_provider_filter*, u_int64_t);* nstat_reporting_allowed;	
  _Bool (void*, void*);* nstat_cookie_equal;	
  size_t (void*, u_int32_t, void*, size_t);* nstat_copy_extension;	

```
#### in6_route_info_64

```c
struct in6_route_info_64 {
  struct in6_addr prefix;
  u_int8_t        prefixlen;
  u_short         defrtrs;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.27

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.27 {
-struct kern_pbufpool* ptr;	
-struct kern_pbufpool* ub;	
-struct kern_pbufpool* lb;	
+struct netif_qset* ptr;	
+struct netif_qset* ub;	
+struct netif_qset* lb;	
 }

```
#### __bounds_safety::wide_ptr.indexable.50

```diff

 struct __bounds_safety::wide_ptr.indexable.50 {
-volatile struct ip* ptr;	
-volatile struct ip* ub;	
+uint8_t* ptr;	
+uint8_t* ub;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.93

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.93 {
-struct flow_demux_pattern* ptr;	
-struct flow_demux_pattern* ub;	
-struct flow_demux_pattern* lb;	
+struct kern_nexus_provider* ptr;	
+struct kern_nexus_provider* ub;	
+struct kern_nexus_provider* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.137

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.137 {
-const struct sadb_key* ptr;	
-const struct sadb_key* ub;	
-const struct sadb_key* lb;	
+struct __kern_packet** ptr;	
+struct __kern_packet** ub;	
+struct __kern_packet** lb;	
 }

```
#### task

```diff

 lck_mtx_t itk_lock_data;	
 struct ipc_port* __ptrauth(DA, true, 0x68c5) itk_task_ports[4];	
 struct ipc_port* __ptrauth(DA, true, 0x4447) itk_settable_self;	
-struct ipc_port* __ptrauth(DA, true, 0x58ef) itk_self;	
 struct exception_action exc_actions[14];	
 struct hardened_exception_action hardened_exception_action;	
 struct ipc_port* __ptrauth(DA, true, 0xbb51) itk_host;	

 counter_t cow_faults;	
 counter_t messages_sent;	
 counter_t messages_received;	
-counter_t pages_grabbed;	
-counter_t pages_grabbed_kern;	
-counter_t pages_grabbed_iopl;	
-counter_t pages_grabbed_upl;	
 uint32_t decompressions;	
 uint32_t syscalls_mach;	
 uint32_t syscalls_unix;	

 mach_vm_address_t all_image_info_addr;	
 mach_vm_size_t all_image_info_size;	
 uint32_t t_kpc;	
+_Atomic darwin_gpu_role_t t_gpu_role;	
 _Bool pidsuspended;	
 _Bool frozen;	
 _Bool changing_freeze_state;	

 uint32_t purged_memory_critical;	
 uint32_t low_mem_privileged_listener;	
 uint32_t mem_notify_reserved;	
-uint32_t memlimit_is_active;	
-uint32_t memlimit_is_fatal;	
-uint32_t memlimit_active_exc_resource;	
-uint32_t memlimit_inactive_exc_resource;	
-uint32_t memlimit_attrs_reserved;	
+_Atomic task_memlimit_flags_t memlimit_flags;	
 io_stat_info_t task_io_stats;	
 struct task_writes_counters task_writes_counters_internal;	
 struct task_writes_counters task_writes_counters_external;	

 unsigned int task_region_info_flags;	
 unsigned int task_has_crossed_thread_limit;	
 unsigned int task_rr_in_flight;	
+unsigned int task_jetsam_realtime_audio;	
 coalition_t coalition[2];	
 queue_chain_t task_coalition[2];	
 uint64_t dispatchqueue_offset;	

```
#### __bounds_safety::wide_ptr.bidi_indexable.65

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.65 {
-volatile uint64_t* ptr;	
-volatile uint64_t* ub;	
-volatile uint64_t* lb;	
+struct netif_flow_head* ptr;	
+struct netif_flow_head* ub;	
+struct netif_flow_head* lb;	
 }

```
#### nxctl_traffic_rule_eth

```c
struct nxctl_traffic_rule_eth {
  struct nxctl_traffic_rule ntre_common;
  struct {
    struct nxctl_traffic_rule_eth *sle_next;
  } ntre_storage_link;
  struct ifnet_traffic_descriptor_eth    ntre_td;
  struct ifnet_traffic_rule_action_steer ntre_ra;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.15

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.15 {
-char* ptr;	
-char* ub;	
-char* lb;	
+struct {
+struct skmem_bufctl* slh_first;	
+}
+* ptr;	
+struct {
+struct skmem_bufctl* slh_first;	
+}
+* ub;	
+struct {
+struct skmem_bufctl* slh_first;	
+}
+* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.128

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.128 {
-struct sk_stats_flow_owner* ptr;	
-struct sk_stats_flow_owner* ub;	
-struct sk_stats_flow_owner* lb;	
+struct ifnet* ptr;	
+struct ifnet* ub;	
+struct ifnet* lb;	
 }

```
#### necp_extra_quic_metadata

```diff

 u_int32_t traffic_mgt_flags;	
 u_int32_t cc_alg_index;	
 u_int32_t state;	
+u_int32_t fallback;	
+u_int32_t unused;	
 u_int8_t ssr_token[16];	
 struct necp_connection_probe_status probestatus;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.53

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.53 {
-struct ip6_hdr* ptr;	
-struct ip6_hdr* ub;	
-struct ip6_hdr* lb;	
+const uint32_t* ptr;	
+const uint32_t* ub;	
+const uint32_t* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.162

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.162 {
-struct netif_qstats_info* ptr;	
-struct netif_qstats_info* ub;	
-struct netif_qstats_info* lb;	
+struct __kern_slot_desc* ptr;	
+struct __kern_slot_desc* ub;	
+struct __kern_slot_desc* lb;	
 }

```
#### ifnet

```diff

  if_ordered_link;	
 lck_mtx_t if_ref_lock;	
 u_int32_t if_refflags;	
-u_int32_t if_refio;	
+os_refcnt_t if_refio;	
 u_int32_t if_threads_pending;	
-u_int32_t if_datamov;	
-u_int32_t if_drainers;	
+os_ref_atomic_t if_datamov;	
 u_int32_t if_suspend;	
 struct ifaddrhead if_addrhead;	
 struct ifaddr* if_lladdr;	

 u_int8_t if_radio_channel;	
 uint8_t network_id[32];	
 uint8_t network_id_len;	
+uint8_t if_l4s_mode;	
 atomic_bool if_mcast_add_signaled;	
 atomic_bool if_mcast_del_signaled;	
-uint32_t if_traffic_rule_count;	
+uint32_t if_inet_traffic_rule_count;	
+uint32_t if_eth_traffic_rule_count;	
 uint32_t if_traffic_rule_genid;	
 uint64_t if_creation_generation_id;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.171

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.171 {
-struct tseg_qent* ptr;	
-struct tseg_qent* ub;	
-struct tseg_qent* lb;	
+struct necp_client_browse_result* ptr;	
+struct necp_client_browse_result* ub;	
+struct necp_client_browse_result* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.80

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.80 {
-struct nxdom* ptr;	
-struct nxdom* ub;	
-struct nxdom* lb;	
+struct __kern_quantum* ptr;	
+struct __kern_quantum* ub;	
+struct __kern_quantum* lb;	
 }

```
#### IOService_CreatePMAssertion_Rpl_With_Content

```c
struct IOService_CreatePMAssertion_Rpl_With_Content {
  IORPCMessageMach                               mach;
  struct IOService_CreatePMAssertion_Rpl_Content content;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.22

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.22 {
-struct skmem_region* ptr;	
-struct skmem_region* ub;	
-struct skmem_region* lb;	
+struct nxctl_get_traffic_rules_iocargs* ptr;	
+struct nxctl_get_traffic_rules_iocargs* ub;	
+struct nxctl_get_traffic_rules_iocargs* lb;	
 }

```
#### IOService_ReleasePMAssertion_Rpl_With_Content

```c
struct IOService_ReleasePMAssertion_Rpl_With_Content {
  IORPCMessageMach                                mach;
  struct IOService_ReleasePMAssertion_Rpl_Content content;
}

```
#### necp_flow_defunct

```diff

 uuid_t flow_id;	
 uuid_t nexus_agent;	
 void* agent_handle;	
+void* socket_handle;	
 int proc_pid;	
 u_int32_t flags;	
 struct necp_client_agent_parameters close_parameters;	

```
#### __bounds_safety::wide_ptr.bidi_indexable.87

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.87 {
-struct kern_pbufpool_u_bft_bkt* ptr;	
-struct kern_pbufpool_u_bft_bkt* ub;	
-struct kern_pbufpool_u_bft_bkt* lb;	
+struct __packet_opt* ptr;	
+struct __packet_opt* ub;	
+struct __packet_opt* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.106

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.106 {
-struct mbuf* ptr;	
-struct mbuf* ub;	
-struct mbuf* lb;	
+struct ifaddr* ptr;	
+struct ifaddr* ub;	
+struct ifaddr* lb;	
 }

```
#### task_ro_data

```diff

 struct task_token_ro_data task_tokens;	
 struct task_filter_ro_data task_filters;	
 uint32_t t_flags_ro;	
-uint32_t task_control_port_options;	
+task_control_port_options_t task_control_port_options;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.92

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.92 {
-struct __kern_buflet* ptr;	
-struct __kern_buflet* ub;	
-struct __kern_buflet* lb;	
+struct netif_port_info* ptr;	
+struct netif_port_info* ub;	
+struct netif_port_info* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.11

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.11 {
-char* ptr;	
-char* ub;	
-char* lb;	
+struct selinfo* ptr;	
+struct selinfo* ub;	
+struct selinfo* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.179

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.179 {
-struct necp_arena_info* ptr;	
-struct necp_arena_info* ub;	
-struct necp_arena_info* lb;	
+struct kern_nexus_provider* ptr;	
+struct kern_nexus_provider* ub;	
+struct kern_nexus_provider* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.100

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.100 {
-struct __kern_buflet_ext* ptr;	
-struct __kern_buflet_ext* ub;	
-struct __kern_buflet_ext* lb;	
+struct netif_queue* ptr;	
+struct netif_queue* ub;	
+struct netif_queue* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.264

```c
struct __bounds_safety::wide_ptr.bidi_indexable.264 {
  nstat_quic_descriptor *ptr;
  nstat_quic_descriptor *ub;
  nstat_quic_descriptor *lb;
}

```
#### net_aop_flow_setup

```c
struct net_aop_flow_setup {
  errno_t(void *, uint32_t, _Bool, uint32_t *);
  *fsp_flow_setup;
  void *fsp_prov_ctx;
}

```
#### _task_ledger_indices

```diff

 int neural_nofootprint_total;	
 int platform_idle_wakeups;	
 int interrupt_wakeups;	
-int sfi_wait_times[17];	
+int sfi_wait_times[18];	
 int cpu_time_billed_to_me;	
 int cpu_time_billed_to_others;	
 int physical_writes;	

 int pages_grabbed_kern;	
 int pages_grabbed_iopl;	
 int pages_grabbed_upl;	
+int est_reclaimable;	
 int fs_metadata_writes;	
 int swapins;	
 }

```
#### _posix_spawnattr

```diff

 uint32_t psa_throttle_timeout;	
 uint32_t psa_kqworkloop_soft_limit;	
 uint32_t psa_kqworkloop_hard_limit;	
+uint32_t psa_conclave_mem_limit;	
 _posix_spawn_port_actions_t psa_ports;	
 _posix_spawn_mac_policy_extensions_t psa_mac_extensions;	
 struct _posix_spawn_coalition_info* psa_coalition_info;	

```
#### __bounds_safety::wide_ptr.bidi_indexable.203

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.203 {
-struct necp_domain_filter* ptr;	
-struct necp_domain_filter* ub;	
-struct necp_domain_filter* lb;	
+channel_ring_stats* ptr;	
+channel_ring_stats* ub;	
+channel_ring_stats* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.259

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.259 {
-struct necp_udp_stats* ptr;	
-struct necp_udp_stats* ub;	
-struct necp_udp_stats* lb;	
+const struct sk_stats_flow* ptr;	
+const struct sk_stats_flow* ub;	
+const struct sk_stats_flow* lb;	
 }

```
#### __bounds_safety::wide_ptr.indexable.104

```diff

 struct __bounds_safety::wide_ptr.indexable.104 {
-void* ptr;	
-void* ub;	
+char* ptr;	
+char* ub;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.62

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.62 {
-struct __user_packet* ptr;	
-struct __user_packet* ub;	
-struct __user_packet* lb;	
+void* ptr;	
+void* ub;	
+void* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.175

```c
struct __bounds_safety::wide_ptr.bidi_indexable.175 {
  struct nexus_controller *ptr;
  struct nexus_controller *ub;
  struct nexus_controller *lb;
}

```
#### _CEKeyValuePair

```c
struct _CEKeyValuePair {
  CEElement_t       derKey;
  CEValueTypePair_t valueTypePair;
}

```
#### vm_object

```diff

 unsigned int vo_ledger_tag;	
 unsigned int vo_no_footprint;	
 uint8_t scan_collisions;	
-uint8_t __object4_unused_bits[1];	
+uint8_t vo_chead_hint;	
+uint8_t __object4_unused_bits;	
 vm_tag_t wire_tag;	
 queue_head_t uplq;	
 queue_chain_t objq;	

```
#### __bounds_safety::wide_ptr.bidi_indexable.148

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.148 {
-struct netif_qstats* ptr;	
-struct netif_qstats* ub;	
-struct netif_qstats* lb;	
+struct netif_llink* ptr;	
+struct netif_llink* ub;	
+struct netif_llink* lb;	
 }

```
#### __bounds_safety::wide_ptr.indexable.40

```diff

 struct __bounds_safety::wide_ptr.indexable.40 {
-struct sksegment_bkt* ptr;	
-struct sksegment_bkt* ub;	
+void* ptr;	
+void* ub;	
 }

```
#### __bounds_safety::wide_ptr.indexable.24

```c
struct __bounds_safety::wide_ptr.indexable.24 {
  volatile struct ip6_hdr *ptr;
  volatile struct ip6_hdr *ub;
}

```
#### __block_literal_23

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- void ();* __FuncPtr;	
+ bool (class OSObject*);* __FuncPtr;	
 struct __block_descriptor* __descriptor;	
-class OSAction* action;	
+class IOPMrootDomain* rootDomain;	
 }

```
#### aop_driver_stats

```c
struct aop_driver_stats {
  uint64_t _arr[4];
}

```
#### zone_security_flags

```diff

 uint32_t z_kheap_id;	
 uint32_t z_kalloc_type;	
 uint32_t z_lifo;	
-uint32_t z_pgz_use_guards;	
 uint32_t z_submap_from_end;	
 uint32_t z_noencrypt;	
 uint32_t z_tag;	

```
#### __bounds_safety::wide_ptr.bidi_indexable.140

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.140 {
-struct skmem_arena* ptr;	
-struct skmem_arena* ub;	
-struct skmem_arena* lb;	
+const struct flow_key* ptr;	
+const struct flow_key* ub;	
+const struct flow_key* lb;	
 }

```
#### _TXMAddressSpace

```diff

 struct _TXMAddressSpace {
 TXMSlabObject_t slabObject;	
 TXMAddressSpaceFlags_t addrSpaceFlags;	
-_Atomic _Bool allowsInvalidCode;	
 CSRestrictedModePerms_t remPerms;	
 TXMAddressSpaceID_t addrSpaceID;	
-TXMReferenceCount_t referenceCount;	
 TXMCodeRegionRBTree_t codeRegions;	
+struct {
+_Atomic _Bool allowsInvalidCode;	
 TXMCodeRegion_t* sharedCacheRegionAllocation;	
 TXMCodeRegion_t* mainRegion;	
 TXMCodeRegion_t* sharedCacheRegion;	
 TXMCodeRegion_t* jitRegion;	
 }
+ ;	
+struct {
+uintptr_t baseAddr;	
+uintptr_t baseAddrEnd;	
+TXMReferenceCount_t referenceCount;	
+}
+ ;	
+}

```
#### protosw

```diff

 struct pr_usrreqs* pr_usrreqs;	
  void (struct protosw*, struct domain*);* pr_init;	
  void ();* pr_drain;	
- int (int*, u_int, void*, size_t*, void*, size_t);* pr_sysctl;	
  int (struct socket*, int, void*);* pr_lock;	
  int (struct socket*, int, void*);* pr_unlock;	
  lck_mtx_t* (struct socket*, int);* pr_getlock;	

 struct protosw_old* pr_old;	
  void (struct socket*, struct proc*, struct proc*);* pr_update_last_owner;	
  void (struct socket*, struct socket*);* pr_copy_last_owner;	
+struct mem_acct* pr_mem_acct;	
 }

```
#### __bounds_safety::wide_ptr.indexable.152

```c
struct __bounds_safety::wide_ptr.indexable.152 {
  char *ptr;
  char *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.207

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.207 {
-struct necp_client_update* ptr;	
-struct necp_client_update* ub;	
-struct necp_client_update* lb;	
+struct necp_domain_filter* ptr;	
+struct necp_domain_filter* ub;	
+struct necp_domain_filter* lb;	
 }

```
#### __bounds_safety::wide_ptr.indexable.98

```c
struct __bounds_safety::wide_ptr.indexable.98 {
  void *ptr;
  void *ub;
}

```
#### IOService_ReleasePMAssertion_Msg

```c
struct IOService_ReleasePMAssertion_Msg {
  IORPCMessageMach           mach;
  mach_msg_port_descriptor_t __object__descriptor;
}

```
#### OSObjectUserVars

```diff

 bool willTerminate;	
 bool didTerminate;	
 bool serverDied;	
+bool instantiated;	
 bool started;	
 bool stopped;	
 bool userServerPM;	

 bool deferredRegisterService;	
 uint32_t powerOverride;	
 IOLock* uvarsLock;	
+class OSDictionary* originalProperties;	
+class OSArray* pmAssertions;	
+class OSArray* pmAssertionsSynced;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.60

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.60 {
-struct __user_quantum* ptr;	
-struct __user_quantum* ub;	
-struct __user_quantum* lb;	
+struct nx_netif* ptr;	
+struct nx_netif* ub;	
+struct nx_netif* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.200

```c
struct __bounds_safety::wide_ptr.bidi_indexable.200 {
  struct nstat_sysinfo_net_api_stats *ptr;
  struct nstat_sysinfo_net_api_stats *ub;
  struct nstat_sysinfo_net_api_stats *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.150

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.150 {
-struct pktq* ptr;	
-struct pktq* ub;	
-struct pktq* lb;	
+struct ip6_moptions_dbg* ptr;	
+struct ip6_moptions_dbg* ub;	
+struct ip6_moptions_dbg* lb;	
 }

```
#### nstat_metrics_req

```c
struct nstat_metrics_req {
  uint32_t mr_version;
  uint32_t mr_id;
}

```
#### __block_literal_27

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- kern_return_t ();* __FuncPtr;	
+ bool (class OSObject*);* __FuncPtr;	
 struct __block_descriptor* __descriptor;	
-class IOServiceStateNotificationDispatchSource* source;	
+class IOUserServerCheckInToken* this;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.48

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.48 {
-struct __kern_packet** ptr;	
-struct __kern_packet** ub;	
-struct __kern_packet** lb;	
+struct skmem_obj* ptr;	
+struct skmem_obj* ub;	
+struct skmem_obj* lb;	
 }

```
#### necp_interface_details

```diff

 u_int32_t hwcsum_flags;	
 u_int8_t radio_type;	
 u_int8_t radio_channel;	
+u_int8_t l4s_mode;	
 }

```
#### __block_literal_32

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- bool (class OSObject*);* __FuncPtr;	
+ void ();* __FuncPtr;	
 struct __block_descriptor_withcopydispose* __descriptor;	
 struct {
 void* __isa;	
 void* __forwarding;	
 int __flags;	
 int __size;	
-kern_return_t kr;	
+lck_rw_type_t lck_rw_type;	
 }
-* kr;	
-class IOService* this;	
-struct IOServiceStateChangeVars* ivars;	
-class IOStateNotificationListener* listener;	
+* lck_rw_type;	
+lck_rw_t* lock;	
 }

```
#### __user_channel_schema

```diff

 const volatile uint32_t csm_flags;	
 char csm_kern_name[256];	
 uuid_t csm_kern_uuid;	
+volatile uint64_t csm_upp_buf_inuse;	
+volatile uint64_t csm_upp_buf_total;	
 uint32_t csm_tx_rings;	
 uint32_t csm_rx_rings;	
 uint32_t csm_allocator_ring_pairs;	

```
#### __bounds_safety::wide_ptr.bidi_indexable.72

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.72 {
-struct kern_nexus_netif_llink_init* ptr;	
-struct kern_nexus_netif_llink_init* ub;	
-struct kern_nexus_netif_llink_init* lb;	
+struct nx_netif_mit* ptr;	
+struct nx_netif_mit* ub;	
+struct nx_netif_mit* lb;	
 }

```
#### __bounds_safety::wide_ptr.indexable.102

```c
struct __bounds_safety::wide_ptr.indexable.102 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### nx_netif

```diff

  errno_t (void*, _Bool);* nif_intf_adv_config;	
 void* nif_intf_adv_prov_ctx;	
 struct netif_qset_extensions nif_qset_extensions;	
+struct netif_rx_flow_steering nif_rx_flow_steering;	
 }

```
#### psemname

```diff

 struct psemname {
 char* psem_nameptr;	
 size_t psem_namelen;	
-u_int32_t psem_hash;	
+uint64_t psem_hash_local;	
+uint64_t psem_hash_global;	
+const char* psem_teamidptr;	
+size_t psem_teamidlen;	
 }

```
#### ip6protosw

```diff

  void (int, struct sockaddr*, void*, struct ifnet*);* pr_ctlinput;	
  int (struct socket*, struct sockopt*);* pr_ctloutput;	
 struct pr_usrreqs* pr_usrreqs;	
- void (struct ip6protosw*, struct domain*);* pr_init;	
+ void (struct protosw*, struct domain*);* pr_init;	
  void ();* pr_drain;	
- int ();* pr_sysctl;	
  int (struct socket*, int, void*);* pr_lock;	
  int (struct socket*, int, void*);* pr_unlock;	
  lck_mtx_t* (struct socket*, int);* pr_getlock;	

 struct protosw_old* pr_old;	
  void (struct socket*, struct proc*, struct proc*);* pr_update_last_owner;	
  void (struct socket*, struct socket*);* pr_copy_last_owner;	
+struct mem_acct* pr_mem_acct;	
 }

```
#### nxctl_traffic_rule_eth_if

```c
struct nxctl_traffic_rule_eth_if {
  char                               rei_ifname[16];
  struct nxctl_traffic_rule_eth_head rei_lists[2];
  uint32_t                           rei_count;
  struct {
    struct nxctl_traffic_rule_eth_if *sle_next;
  } rei_link;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.217

```c
struct __bounds_safety::wide_ptr.bidi_indexable.217 {
  struct necp_client_observer_update *ptr;
  struct necp_client_observer_update *ub;
  struct necp_client_observer_update *lb;
}

```
#### upl_fs_verify_info

```c
struct upl_fs_verify_info {
  uint8_t *verify_data_ptr;
  uint32_t verify_data_len;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.8

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.8 {
-void* ptr;	
-void* ub;	
-void* lb;	
+struct nxctl_traffic_rule_type* ptr;	
+struct nxctl_traffic_rule_type* ub;	
+struct nxctl_traffic_rule_type* lb;	
 }

```
#### ipc_service_port_label

```diff

 struct ipc_service_port_label {
-void* __ptrauth(DA, true, 0xa6b2) ispl_sblabel;	
+struct ipc_conn_port_label* __ptrauth(DA, true, 0xa6b2) ispl_sblabel;	
 mach_port_context_t ispl_launchd_context;	
 mach_port_name_t ispl_launchd_name;	
-ipc_service_port_label_flags_t ispl_flags;	
+uint8_t ispl_bootstrap_port;	
+uint8_t ispl_throttled;	
+uint8_t __ispl_unused;	
 uint8_t ispl_domain;	
 char* ispl_service_name;	
 }

```
#### proc_ro

```diff

 struct task_token_ro_data task_tokens;	
 struct task_filter_ro_data task_filters;	
 uint32_t t_flags_ro;	
-uint32_t task_control_port_options;	
+task_control_port_options_t task_control_port_options;	
 }
  ;	
 struct task_ro_data task_data;	

```
#### __bounds_safety::wide_ptr.bidi_indexable.193

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.193 {
-nstat_msg_add_src_req* ptr;	
-nstat_msg_add_src_req* ub;	
-nstat_msg_add_src_req* lb;	
+struct ether_header* ptr;	
+struct ether_header* ub;	
+struct ether_header* lb;	
 }

```
#### vsock_transport

```diff

 struct vsock_transport {
+uint16_t protocol;	
 void* provider;	
  int (void*, uint32_t*);* get_cid;	
  int (void*);* attach_socket;	

```
#### vm_map_links

```diff

 struct vm_map_links {
-struct vm_map_entry* prev;	
+uintptr_t prev;	
+uint8_t vme_zero_wire_count_waiters;	
 struct vm_map_entry* next;	
 vm_map_offset_t start;	
 vm_map_offset_t end;	

```
#### __bounds_safety::wide_ptr.bidi_indexable.59

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.59 {
-struct __kern_packet** ptr;	
-struct __kern_packet** ub;	
-struct __kern_packet** lb;	
+struct skmem_obj_info* ptr;	
+struct skmem_obj_info* ub;	
+struct skmem_obj_info* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.75

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.75 {
-struct __kern_quantum* ptr;	
-struct __kern_quantum* ub;	
-struct __kern_quantum* lb;	
+struct mbuf* ptr;	
+struct mbuf* ub;	
+struct mbuf* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.55

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.55 {
-struct kalloc_type_view* ptr;	
-struct kalloc_type_view* ub;	
-struct kalloc_type_view* lb;	
+struct __kern_packet** ptr;	
+struct __kern_packet** ub;	
+struct __kern_packet** lb;	
 }

```
#### nstat_client_info

```c
struct nstat_client_info {
  struct nstat_client_details nstat_client_details;
  struct nstat_metrics        nstat_metrics;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.136

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.136 {
-struct mbuf* ptr;	
-struct mbuf* ub;	
-struct mbuf* lb;	
+struct ip6_hdr* ptr;	
+struct ip6_hdr* ub;	
+struct ip6_hdr* lb;	
 }

```
#### vm_page_with_ppnum

```c
struct vm_page_with_ppnum {
  struct vm_page vmp_page;
  ppnum_t        vmp_phys_page;
}

```
#### __block_literal_18

```diff

 int __flags;	
 int __reserved;	
  bool (class OSObject*);* __FuncPtr;	
-struct __block_descriptor* __descriptor;	
+struct __block_descriptor_withcopydispose* __descriptor;	
+struct {
+void* __isa;	
+void* __forwarding;	
+int __flags;	
+int __size;	
+bool allPowerStates;	
+}
+* allPowerStates;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.97

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.97 {
-struct ucred* ptr;	
-struct ucred* ub;	
-struct ucred* lb;	
+const struct __kern_buflet* ptr;	
+const struct __kern_buflet* ub;	
+const struct __kern_buflet* lb;	
 }

```
#### ipc_kobject_ops

```diff

 ipc_kobject_type_t iko_op_type;	
 unsigned long iko_op_stable;	
 unsigned long iko_op_permanent;	
+unsigned long iko_op_movable_send;	
 const char* iko_op_name;	
  void (ipc_port_t, mach_port_mscount_t);* iko_op_no_senders;	
- void (ipc_port_t);* iko_op_destroy;	
+ void (ipc_object_label_t);* iko_op_label_free;	
 }

```
#### __bounds_safety::wide_ptr.indexable.115

```c
struct __bounds_safety::wide_ptr.indexable.115 {
  void *ptr;
  void *ub;
}

```
#### bufattr

```diff

 uint64_t ba_cp_file_off;	
 uint64_t ba_flags;	
 void* ba_verify_ctx;	
+vnode_verify_kind_t ba_verify_type;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.91

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.91 {
-struct __kern_buflet* ptr;	
-struct __kern_buflet* ub;	
-struct __kern_buflet* lb;	
+struct __user_buflet* ptr;	
+struct __user_buflet* ub;	
+struct __user_buflet* lb;	
 }

```
#### __bounds_safety::wide_ptr.indexable.36

```diff

 struct __bounds_safety::wide_ptr.indexable.36 {
-char* ptr;	
-char* ub;	
+struct skmem_bufctl* ptr;	
+struct skmem_bufctl* ub;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.143

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.143 {
-struct __kern_slot_desc* ptr;	
-struct __kern_slot_desc* ub;	
-struct __kern_slot_desc* lb;	
+struct in_ifaddr* ptr;	
+struct in_ifaddr* ub;	
+struct in_ifaddr* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.160

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.160 {
-struct tcphdr* ptr;	
-struct tcphdr* ub;	
-struct tcphdr* lb;	
+struct nx_llink_info_req* ptr;	
+struct nx_llink_info_req* ub;	
+struct nx_llink_info_req* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.157

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.157 {
-struct kalloc_heap* ptr;	
-struct kalloc_heap* ub;	
-struct kalloc_heap* lb;	
+struct keycb* ptr;	
+struct keycb* ub;	
+struct keycb* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.123

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.123 {
-struct mbuf* ptr;	
-struct mbuf* ub;	
-struct mbuf* lb;	
+const struct esp_algorithm* ptr;	
+const struct esp_algorithm* ub;	
+const struct esp_algorithm* lb;	
 }

```
#### __block_literal_22

```diff

 int __flags;	
 int __reserved;	
  bool (class OSObject*);* __FuncPtr;	
-struct __block_descriptor* __descriptor;	
-class IOService* client;	
+struct __block_descriptor_withcopydispose* __descriptor;	
+struct {
+void* __isa;	
+void* __forwarding;	
+int __flags;	
+int __size;	
+bool allPowerStates;	
+}
+* allPowerStates;	
 }

```
#### netmask_rn_entry

```c
struct netmask_rn_entry {
  struct rn_base_entry nrn_base;
  char                 nrn_netmask[32];
}

```
#### net_aop_provider_init

```c
struct net_aop_provider_init {
  uint32_t kaopi_version;
  errno_t(void *, net_aop_capab_t, void *, uint32_t *);
  *kaopi_config_capab;
}

```
#### __bounds_safety::wide_ptr.indexable.168

```c
struct __bounds_safety::wide_ptr.indexable.168 {
  struct nstat_msg_src_description *ptr;
  struct nstat_msg_src_description *ub;
}

```
#### __block_literal_25

```diff

 int __flags;	
 int __reserved;	
  bool (class OSObject*);* __FuncPtr;	
-struct __block_descriptor_withcopydispose* __descriptor;	
-struct {
-void* __isa;	
-void* __forwarding;	
-int __flags;	
-int __size;	
-class IOUserServerCheckInToken* result;	
-}
-* result;	
-const class OSSymbol* serverName;	
+struct __block_descriptor* __descriptor;	
+class IOService* client;	
 }

```
#### nstat_sock_locus

```c
struct nstat_sock_locus {
  nstat_locus            nsl_locus;
  tailq_entry_sock_locus nsl_link;
  struct inpcb          *nsl_inp;
  uint32_t               nsl_magic;
  pid_t                  nsl_pid;
  uint32_t               nsl_ifnet_properties;
  char                   nsl_pname[33];
  char                   nsl_is_tcp;
}

```
#### __block_literal_30

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- bool (const class OSSymbol*, class OSObject*);* __FuncPtr;	
+ kern_return_t ();* __FuncPtr;	
 struct __block_descriptor* __descriptor;	
-class OSDictionary* result;	
+class IOServiceStateNotificationDispatchSource* source;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.153

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.153 {
-struct kern_nexus_domain_provider* ptr;	
-struct kern_nexus_domain_provider* ub;	
-struct kern_nexus_domain_provider* lb;	
+struct pktq* ptr;	
+struct pktq* ub;	
+struct pktq* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.161

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.161 {
-uint8_t* ptr;	
-uint8_t* ub;	
-uint8_t* lb;	
+struct kalloc_heap* ptr;	
+struct kalloc_heap* ub;	
+struct kalloc_heap* lb;	
 }

```
#### memorystatus_system_health

```diff

 struct memorystatus_system_health {
+_Bool msh_vm_pressure_warning;	
+_Bool msh_vm_pressure_critical;	
 _Bool msh_compressor_exhausted;	
 _Bool msh_swap_exhausted;	
 _Bool msh_swap_low_on_space;	

```
#### __bounds_safety::wide_ptr.bidi_indexable.64

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.64 {
-struct nexus_adapter* ptr;	
-struct nexus_adapter* ub;	
-struct nexus_adapter* lb;	
+struct kalloc_type_view* ptr;	
+struct kalloc_type_view* ub;	
+struct kalloc_type_view* lb;	
 }

```
#### kern_nexus_capab_rx_flow_steering

```c
struct kern_nexus_capab_rx_flow_steering {
  uint32_t kncrxfs_version;
  void    *kncrxfs_prov_ctx;
  errno_t(void *, uint32_t, struct ifnet_traffic_descriptor_common *, uint32_t);
  *kncrxfs_config;
}

```
#### thread

```diff

 _Bool th_shared_rsrc_enqueued[2];	
 _Bool th_shared_rsrc_heavy_user[2];	
 _Bool th_shared_rsrc_heavy_perf_control[2];	
+uint8_t th_expired_quantum_on_lower_core;	
+uint8_t th_expired_quantum_on_higher_core;	
 struct priority_queue_entry_stable th_clutch_runq_link;	
 struct priority_queue_entry_sched th_clutch_pri_link;	
 queue_chain_t th_clutch_timeshare_link;	

 mach_msg_size_t msize;	
 mach_msg_size_t asize;	
 mach_port_name_t receiver_name;	
-union {
 struct ipc_kmsg* __ptrauth(DA, true, 0x33ff) kmsg;	
-}
- ;	
 }
  receive;	
 struct {

```
#### __bounds_safety::wide_ptr.bidi_indexable.156

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.156 {
-struct nx_llink_info_req* ptr;	
-struct nx_llink_info_req* ub;	
-struct nx_llink_info_req* lb;	
+struct kern_nexus_domain_provider* ptr;	
+struct kern_nexus_domain_provider* ub;	
+struct kern_nexus_domain_provider* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.196

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.196 {
-struct skmem_cache* ptr;	
-struct skmem_cache* ub;	
-struct skmem_cache* lb;	
+struct nstat_sysinfo_lim_stats* ptr;	
+struct nstat_sysinfo_lim_stats* ub;	
+struct nstat_sysinfo_lim_stats* lb;	
 }

```
#### __bounds_safety::wide_ptr.indexable.244

```c
struct __bounds_safety::wide_ptr.indexable.244 {
  struct necp_client_add_flow *ptr;
  struct necp_client_add_flow *ub;
}

```
#### nxctl_traffic_rule_eth_iocinfo

```c
struct nxctl_traffic_rule_eth_iocinfo {
  struct nxctl_traffic_rule_generic_iocinfo tre_common;
  struct ifnet_traffic_descriptor_eth       tre_td;
  struct ifnet_traffic_rule_action_steer    tre_ra;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.233

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.233 {
-struct necp_drop_dest_entry* ptr;	
-struct necp_drop_dest_entry* ub;	
-struct necp_drop_dest_entry* lb;	
+struct nstat_counts* ptr;	
+struct nstat_counts* ub;	
+struct nstat_counts* lb;	
 }

```
#### tcpcb

```diff

 uint32_t rcv_wnd;	
 uint32_t t_last_recwin;	
 tcp_seq rcv_up;	
+uint32_t t_latest_tx;	
 uint32_t snd_wnd;	
 uint32_t snd_cwnd;	
 uint32_t snd_ssthresh;	

 int t_softerror;	
 char t_oobflags;	
 char t_iobc;	
-u_int8_t snd_scale;	
-u_int8_t rcv_scale;	
-u_int8_t request_r_scale;	
-u_int8_t requested_s_scale;	
-u_int8_t tcp_cc_index;	
-u_int8_t t_adaptive_rtimo;	
-u_int8_t t_adaptive_wtimo;	
-u_int8_t t_stretchack_delayed;	
-u_int16_t t_early_rexmt_count;	
-u_int32_t t_early_rexmt_win;	
-u_int32_t ts_recent;	
-u_int32_t ts_recent_age;	
+uint8_t snd_scale;	
+uint8_t rcv_scale;	
+uint8_t request_r_scale;	
+uint8_t requested_s_scale;	
+uint8_t tcp_cc_index;	
+uint8_t t_adaptive_rtimo;	
+uint8_t t_adaptive_wtimo;	
+uint16_t t_early_rexmt_count;	
+uint32_t t_early_rexmt_win;	
+uint32_t ts_recent;	
+uint32_t t_ts_offset;	
+uint32_t ts_recent_age;	
 tcp_seq last_ack_sent;	
 uint32_t t_bytes_acked;	
 uint32_t total_ect_packets_marked;	

 uint32_t t_persist_timeout;	
 uint32_t t_persist_stop;	
 uint32_t t_notsent_lowat;	
-u_int32_t rcv_unackwin;	
-u_int32_t rcv_by_unackwin;	
-u_int32_t rcv_by_unackhalfwin;	
-u_int32_t rcv_nostrack_ts;	
-u_int32_t rcv_nostrack_pkts;	
-u_int16_t rcv_waitforss;	
-u_int32_t ecn_flags;	
-u_int32_t t_ecn_recv_ce;	
-u_int32_t t_ecn_recv_cwr;	
+uint32_t ecn_flags;	
+uint32_t t_ecn_recv_ce;	
+uint32_t t_ecn_recv_cwr;	
 uint32_t t_client_accecn_state;	
 uint32_t t_server_accecn_state;	
 uint64_t t_ecn_capable_packets_sent;	

 uint8_t t_prev_ip_ecn;	
 struct accecn t_aecn;	
 struct pacer t_pacer;	
-u_int32_t snd_cwnd_prev;	
-u_int32_t snd_ssthresh_prev;	
+uint32_t snd_cwnd_prev;	
+uint32_t snd_ssthresh_prev;	
 tcp_seq snd_recover_prev;	
 int t_srtt_prev;	
 int t_rttvar_prev;	
-u_int32_t t_badrexmt_time;	
-u_int32_t t_reorderwin;	
+uint32_t t_badrexmt_time;	
+uint32_t t_reorderwin;	
 int16_t snd_numholes;	
 struct sackhole_head snd_holes;	
 tcp_seq snd_fack;	

 struct sackhint sackhint;	
 struct mbuf* t_pktlist_head;	
 struct mbuf* t_pktlist_tail;	
-u_int32_t t_pktlist_sentlen;	
-u_int32_t t_keepidle;	
-u_int32_t t_keepinit;	
-u_int32_t t_keepintvl;	
-u_int32_t t_keepcnt;	
-u_int32_t tso_max_segment_size;	
-u_int16_t t_pmtud_lastseg_size;	
-u_int32_t t_pmtud_saved_maxopd;	
-u_int32_t t_pmtud_start_ts;	
+uint32_t t_pktlist_sentlen;	
+uint32_t t_keepidle;	
+uint32_t t_keepinit;	
+uint32_t t_keepintvl;	
+uint32_t t_keepcnt;	
+uint32_t tso_max_segment_size;	
+uint16_t t_pmtud_lastseg_size;	
+uint32_t t_pmtud_saved_maxopd;	
+uint32_t t_pmtud_start_ts;	
 struct {
-u_int32_t rxduplicatebytes;	
-u_int32_t rxoutoforderbytes;	
-u_int32_t txretransmitbytes;	
-u_int16_t synrxtshift;	
-u_int16_t rxmitsyns;	
-u_int16_t unused_pad_to_8;	
-u_int32_t rxmitpkts;	
+uint32_t rxduplicatebytes;	
+uint32_t rxoutoforderbytes;	
+uint32_t txretransmitbytes;	
+uint16_t synrxtshift;	
+uint16_t rxmitsyns;	
+uint16_t unused_pad_to_8;	
+uint32_t rxmitpkts;	
 uint32_t delayed_acks_sent;	
 uint32_t acks_delayed;	
+uint64_t bytes_acked;	
 }
  t_stat;	
-u_int8_t t_syn_sent;	
-u_int8_t t_syn_rcvd;	
-u_int8_t t_notify_ack_count;	
-u_int8_t t_ecn_recv_ce_pkt;	
-u_int32_t t_cached_maxopd;	
+uint8_t t_syn_sent;	
+uint8_t t_syn_rcvd;	
+uint8_t t_notify_ack_count;	
+uint8_t t_ecn_recv_ce_pkt;	
+uint32_t t_cached_maxopd;	
 uint32_t bg_ssthresh;	
 uint32_t t_flagsext;	
 uint32_t iaj_rcv_ts;	

 uint32_t t_rxt_seg_count;	
 uint32_t t_rxt_seg_drop;	
 tcp_seq t_dsack_lastuna;	
-u_int32_t t_pipeack_sample[3];	
+uint32_t t_pipeack_sample[3];	
 tcp_seq t_pipeack_lastuna;	
-u_int32_t t_pipeack;	
-u_int32_t t_lossflightsize;	
-u_int32_t t_mpflags;	
+uint32_t t_pipeack;	
+uint32_t t_lossflightsize;	
+uint32_t t_mpflags;	
 tcp_seq t_mpuna;	
 struct mptcb* t_mptcb;	
 struct mptsub* t_mpsub;	
-struct mpt_dsn_map t_rcv_map;	
-u_int8_t t_local_aid;	
-u_int8_t t_rem_aid;	
-u_int8_t t_mprxtshift;	
-u_int8_t t_tfo_flags;	
-u_int16_t t_tfo_stats;	
-u_int8_t t_tfo_probes;	
-u_int8_t t_tfo_probe_state;	
-u_int32_t t_rcvoopack;	
-u_int32_t t_pawsdrop;	
-u_int32_t t_sack_recovery_episode;	
+uint8_t t_local_aid;	
+uint8_t t_rem_aid;	
+uint8_t t_mprxtshift;	
+uint8_t t_tfo_flags;	
+uint16_t t_tfo_stats;	
+uint8_t t_tfo_probes;	
+uint8_t t_tfo_probe_state;	
+uint32_t t_rcvoopack;	
+uint32_t t_pawsdrop;	
+uint32_t t_sack_recovery_episode;	
 uint32_t t_rack_recovery_episode;	
 uint32_t t_rack_reo_timeout_recovery_episode;	
-u_int32_t t_reordered_pkts;	
-u_int32_t t_dsack_sent;	
-u_int32_t t_dsack_recvd;	
+uint32_t t_reordered_pkts;	
+uint32_t t_dsack_sent;	
+uint32_t t_dsack_recvd;	
 struct {
 struct tcp_notify_ack_marker* slh_first;	
 }
  t_notify_ack;	
-u_int32_t t_recv_throttle_ts;	
-u_int32_t t_rxt_minimum_timeout;	
+uint32_t t_recv_throttle_ts;	
+uint32_t t_rxt_minimum_timeout;	
 uint32_t t_challengeack_last;	
 uint32_t t_challengeack_count;	
-u_int32_t t_connect_time;	
+uint32_t t_connect_time;	
 uint64_t t_rcvwnd_limited_total_time;	
 uint64_t t_rcvwnd_limited_start_time;	
 uint32_t t_comp_rxmt_gencnt;	
 uint32_t t_comp_ack_gencnt;	
 uint32_t t_comp_ack_lastinc;	
-uint32_t t_ts_offset;	
 uint32_t curr_rtt_hist[4];	
 uint32_t curr_rtt_min;	
 uint32_t curr_rtt_index;	

 uint32_t bytes_lost;	
 uint32_t bytes_retransmitted;	
 uint32_t bytes_sacked;	
+uint8_t l4s_enabled;	
+uint8_t accurate_ecn_on;	
+uint8_t _pad;	
 uuid_t t_fsw_uuid;	
 uuid_t t_flow_uuid;	
 }

```
#### aop_activity_bitmap

```c
struct aop_activity_bitmap {
  uint64_t start;
  uint64_t bitmap[8];
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.122

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.122 {
-ctrace_t* ptr;	
-ctrace_t* ub;	
-ctrace_t* lb;	
+struct nx_flowswitch* ptr;	
+struct nx_flowswitch* ub;	
+struct nx_flowswitch* lb;	
 }

```
#### __bounds_safety::wide_ptr.indexable.72

```diff

 struct __bounds_safety::wide_ptr.indexable.72 {
-char* ptr;	
-char* ub;	
+void* ptr;	
+void* ub;	
 }

```
#### ledger_template

```diff

 uint16_t lt_table_size;	
 struct entry_template* lt_entries;	
 uint16_t* lt_entries_lut;	
+uint16_t lt_counters;	
+uint16_t lt_counter_offset;	
+zone_t lt_counter_zone;	
+char lt_counter_zone_name[32];	
 }

```
#### aop_buffer

```c
struct aop_buffer {
  uint32_t bufsize;
  uint32_t bufused;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.12

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.12 {
-void* ptr;	
-void* ub;	
-void* lb;	
+char* ptr;	
+char* ub;	
+char* lb;	
 }

```
#### trap_debounce_buffer

```c
struct trap_debounce_buffer {
  match_record_s records[2];
  size_t         tail;
}

```
#### traffic_stats

```c
struct traffic_stats {
  uint64_t          ts_rxpackets;
  uint64_t          ts_rxbytes;
  uint64_t          ts_txpackets;
  uint64_t          ts_txbytes;
  activity_bitmap_t ts_bitmap;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.83

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.83 {
-struct kern_channel* ptr;	
-struct kern_channel* ub;	
-struct kern_channel* lb;	
+struct __packet_opt* ptr;	
+struct __packet_opt* ub;	
+struct __packet_opt* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.36

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.36 {
-struct nxprov_params* ptr;	
-struct nxprov_params* ub;	
-struct nxprov_params* lb;	
+uint64_t* ptr;	
+uint64_t* ub;	
+uint64_t* lb;	
 }

```
#### __block_literal_24

```diff

 int __reserved;	
  bool (class OSObject*);* __FuncPtr;	
 struct __block_descriptor* __descriptor;	
-class IOUserServerCheckInToken* this;	
+class IOPMrootDomain* rootDomain;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.169

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.169 {
-struct flow_owner* ptr;	
-struct flow_owner* ub;	
-struct flow_owner* lb;	
+necp_application_id_t* ptr;	
+necp_application_id_t* ub;	
+necp_application_id_t* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.101

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.101 {
-struct sockaddr_dl* ptr;	
-struct sockaddr_dl* ub;	
-struct sockaddr_dl* lb;	
+struct kern_nexus_provider* ptr;	
+struct kern_nexus_provider* ub;	
+struct kern_nexus_provider* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.215

```c
struct __bounds_safety::wide_ptr.bidi_indexable.215 {
  struct necp_client_update *ptr;
  struct necp_client_update *ub;
  struct necp_client_update *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.49

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.49 {
-struct mbuf** ptr;	
-struct mbuf** ub;	
-struct mbuf** lb;	
+uint32_t* ptr;	
+uint32_t* ub;	
+uint32_t* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.133

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.133 {
-struct flow_route_bucket* ptr;	
-struct flow_route_bucket* ub;	
-struct flow_route_bucket* lb;	
+struct flow_owner_bucket* ptr;	
+struct flow_owner_bucket* ub;	
+struct flow_owner_bucket* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.152

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.152 {
-struct sadb_alg* ptr;	
-struct sadb_alg* ub;	
-struct sadb_alg* lb;	
+struct netif_queue* ptr;	
+struct netif_queue* ub;	
+struct netif_queue* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.77

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.77 {
-void* ptr;	
-void* ub;	
-void* lb;	
+struct netif_stats* ptr;	
+struct netif_stats* ub;	
+struct netif_stats* lb;	
 }

```
#### IOService_StateNotificationItemCreate_Msg_Content

```diff

 IORPCMessage __hdr;	
 OSObjectRef __object;	
 class OSString* itemName;	
-class OSDictionary* schema;	
+class OSDictionary* value;	
 }

```
#### _ca_event_latency_violations

```c
struct _ca_event_latency_violations {
  ca_sstr            backtrace[256];
  ca_sstr            kernel_platform[12];
  ca_sstr            uuid[37];
  unsigned long long violation_code;
  unsigned long long violation_cpi;
  ca_sstr            violation_cpu_type[2];
  unsigned long long violation_duration;
  unsigned long long violation_freq;
  unsigned long long violation_payload;
  unsigned long long violation_threshold;
}

```
#### ipc_policy_violations_rb_entry

```diff

 char signing_id[128];	
 ipc_policy_violation_id_t violation_id;	
 int sw_platform;	
-int msgh_id;	
+int aux_data;	
 int sdk;	
 }

```
#### mptsub

```diff

 uint32_t mpts_probesoon;	
 uint32_t mpts_probecnt;	
 uint32_t mpts_maxseg;	
+struct mpt_dsn_map mpts_rcv_map;	
 }

```
#### __bounds_safety::wide_ptr.indexable.122

```c
struct __bounds_safety::wide_ptr.indexable.122 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### fq_codel_sched_data

```diff

 struct thread_call* fqs_pacemaker_tcall;	
 bitmap_ops_t* fqs_bm_ops;	
 fq_if_group_t* fqs_classq_groups[16];	
+ int (void*, fq_if_group_t*, pktsched_pkt_t*, fq_if_classq_t*);* fqs_enqueue;	
+ void (void*, void*, pktsched_pkt_t*, uint64_t);* fqs_dequeue;	
+ifcq_oid_t fqs_oid;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.270

```c
struct __bounds_safety::wide_ptr.bidi_indexable.270 {
  nstat_interface_counts *ptr;
  nstat_interface_counts *ub;
  nstat_interface_counts *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.190

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.190 {
-struct __kern_packet* ptr;	
-struct __kern_packet* ub;	
-struct __kern_packet* lb;	
+struct __kern_netif_intf_advisory* ptr;	
+struct __kern_netif_intf_advisory* ub;	
+struct __kern_netif_intf_advisory* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.164

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.164 {
-struct fileglob* ptr;	
-struct fileglob* ub;	
-struct fileglob* lb;	
+struct ifnet_keepalive_offload_frame* ptr;	
+struct ifnet_keepalive_offload_frame* ub;	
+struct ifnet_keepalive_offload_frame* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.84

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.84 {
-struct __user_buflet* ptr;	
-struct __user_buflet* ub;	
-struct __user_buflet* lb;	
+struct flow_mgr* ptr;	
+struct flow_mgr* ub;	
+struct flow_mgr* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.56

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.56 {
-uint8_t* ptr;	
-uint8_t* ub;	
-uint8_t* lb;	
+struct mbuf** ptr;	
+struct mbuf** ub;	
+struct mbuf** lb;	
 }

```
#### zone

```diff

 uint32_t no_callout;	
 uint32_t z_destructible;	
 uint32_t _reserved;	
-uint32_t z_pgz_tracked;	
-uint32_t z_pgz_use_guards;	
 uint32_t z_kasan_fakestacks;	
 uint32_t z_kasan_quarantine;	
 uint32_t z_tags_sizeclass;	

```
#### __bounds_safety::wide_ptr.bidi_indexable.191

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.191 {
-struct nstat_msg_hdr* ptr;	
-struct nstat_msg_hdr* ub;	
-struct nstat_msg_hdr* lb;	
+struct pf_rulequeue* ptr;	
+struct pf_rulequeue* ub;	
+struct pf_rulequeue* lb;	
 }

```
#### conninfo_mptcp

```diff

 uint64_t mptcpci_lidsn;	
 uint32_t mptcpci_sndwnd;	
 uint64_t mptcpci_rcvnxt;	
-uint64_t mptcpci_rcvatmark;	
 uint64_t mptcpci_ridsn;	
 uint32_t mptcpci_rcvwnd;	
 uint8_t mptcpci_mpte_addrid;	

```
#### _load_result

```diff

 mach_vm_address_t ro_vm_start;	
 mach_vm_address_t ro_vm_end;	
 unsigned int platform_binary;	
-HR_flags_t hardened_runtime_binary;	
+enhanced_security_flags_t enhanced_security_binary;	
 off_t cs_end_offset;	
 void* threadstate;	
 size_t threadstate_sz;	

```
#### mach_vm_reclaim_update_kernel_accounting_trap_args

```c
struct mach_vm_reclaim_update_kernel_accounting_trap_args {
  char             target_task_l_[0];
  mach_port_name_t target_task;
  char             target_task_r_[4];
  char             bytes_reclaimed_out_l_[0];
  user_addr_t      bytes_reclaimed_out;
  char             bytes_reclaimed_out_r_[0];
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.104

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.104 {
-struct __kern_packet* ptr;	
-struct __kern_packet* ub;	
-struct __kern_packet* lb;	
+struct sockaddr* ptr;	
+struct sockaddr* ub;	
+struct sockaddr* lb;	
 }

```
#### mem_acct

```c
struct mem_acct {
  _Atomic int64_t  ma_allocated;
  int32_t         *ma_percpu;
  uint64_t         ma_hardlimit;
  uint8_t          ma_percent;
  _Atomic uint64_t ma_peak;
  char             ma_name[16];
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.61

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.61 {
-uint16_t* ptr;	
-uint16_t* ub;	
-uint16_t* lb;	
+struct kalloc_type_view* ptr;	
+struct kalloc_type_view* ub;	
+struct kalloc_type_view* lb;	
 }

```
#### nstat_metrics

```diff

 uint32_t nstat_query_description_nobuf;	
 uint32_t nstat_query_description_yield;	
 uint32_t nstat_query_description_limit;	
+uint32_t nstat_query_details_nobuf;	
+uint32_t nstat_query_details_upgrade;	
+uint32_t nstat_query_details_noupgrade;	
+uint32_t nstat_query_details_yield;	
+uint32_t nstat_query_details_limit;	
+uint32_t nstat_query_details_all;	
+uint32_t nstat_query_details_one;	
 uint32_t nstat_query_update_nobuf;	
 uint32_t nstat_query_update_upgrade;	
 uint32_t nstat_query_update_noupgrade;	

 uint32_t nstat_src_add_no_src_mem;	
 uint32_t nstat_src_add_send_err;	
 uint32_t nstat_src_add_while_cleanup;	
+uint32_t nstat_add_all_tcp_skip_dead;	
+uint32_t nstat_add_all_udp_skip_dead;	
+uint32_t nstat_src_goodbye_successes;	
+uint32_t nstat_src_goodbye_failures;	
+uint32_t nstat_src_goodbye_sent_details;	
+uint32_t nstat_src_goodbye_failed_details;	
+uint32_t nstat_src_goodbye_filtered_details;	
+uint32_t nstat_src_goodbye_sent_update;	
+uint32_t nstat_src_goodbye_failed_update;	
+uint32_t nstat_src_goodbye_filtered_update;	
+uint32_t nstat_src_goodbye_sent_counts;	
+uint32_t nstat_src_goodbye_failed_counts;	
+uint32_t nstat_src_goodbye_filtered_counts;	
+uint32_t nstat_src_goodbye_sent_description;	
+uint32_t nstat_src_goodbye_failed_description;	
+uint32_t nstat_src_goodbye_sent_removed;	
+uint32_t nstat_src_goodbye_failed_removed;	
+uint32_t nstat_src_goodbye_filtered_removed;	
+uint32_t nstat_pcb_event;	
+uint32_t nstat_send_event;	
+uint32_t nstat_send_event_fail;	
+uint32_t nstat_send_event_notsup;	
+uint32_t nstat_route_src_gone_idlecheck;	
+uint32_t nstat_src_removed_linkage;	
 uint32_t nstat_src_gone_idlecheck;	
 uint32_t nstat_last_uint32_count;	
 uint32_t nstat_stats_pad;	

```
#### if_ifclassq_stats

```diff

 struct pktcntr ifqs_xmitcnt;	
 struct pktcntr ifqs_dropcnt;	
 u_int32_t ifqs_scheduler;	
+union {
 struct fq_codel_classstats ifqs_fq_codel_stats;	
 }
+ ;	
+}

```
#### _TXMReadOnlyData

```diff

 _Bool MTESupported;	
 struct {
 _Bool research;	
+_Bool extendedResearch;	
 TXMBuildType_t variant;	
 }
  buildType;	
 struct {
 _Bool virtualized;	
+TXMDeviceFusing_t fusing;	
 TXMDeviceType_t platform;	
 }
  deviceType;	

 CSConfig_t CSConfiguration;	
 EntitlementsContext_t localSigningEntitlementsCtx;	
 CSRestrictedModeState_t* restrictedModeState;	
-uintptr_t sharedRegionsBaseAddr;	
-uintptr_t sharedRegionsBaseAddrEnd;	
 const char* bootArgs;	
 const _Bool* kernelTriggeredPanic;	
 uint32_t maxCPUs;	

 _Bool bringUpMode;	
 _Bool relaxTrustCacheAttestationForREM;	
 _Bool emulatedUdid;	
-_Bool allowSelfJIT;	
 TXMExemptionDeviceState_t deviceState;	
 }
  exemptions;	

```
#### __bounds_safety::wide_ptr.bidi_indexable.155

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.155 {
-const struct __kern_packet** ptr;	
-const struct __kern_packet** ub;	
-const struct __kern_packet** lb;	
+struct sav_dump_elem* ptr;	
+struct sav_dump_elem* ub;	
+struct sav_dump_elem* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.70

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.70 {
-struct __kern_slot_desc* ptr;	
-struct __kern_slot_desc* ub;	
-struct __kern_slot_desc* lb;	
+volatile uint64_t* ptr;	
+volatile uint64_t* ub;	
+volatile uint64_t* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.20

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.20 {
-struct kalloc_type_view* ptr;	
-struct kalloc_type_view* ub;	
-struct kalloc_type_view* lb;	
+struct nxctl_remove_traffic_rule_iocargs* ptr;	
+struct nxctl_remove_traffic_rule_iocargs* ub;	
+struct nxctl_remove_traffic_rule_iocargs* lb;	
 }

```
#### __bounds_safety::wide_ptr.indexable.209

```c
struct __bounds_safety::wide_ptr.indexable.209 {
  struct nstat_msg_add_src *ptr;
  struct nstat_msg_add_src *ub;
}

```
#### workq_aio_uthread_head

```c
struct workq_aio_uthread_head {
  struct uthread  *tqh_first;
  struct uthread **tqh_last;
}

```
#### socket

```diff

 void* so_eventarg;	
 kauth_cred_t so_cred;	
 so_gen_t so_gencnt;	
-struct {
-struct socket* stqe_next;	
-}
- so_cache_ent;	
-caddr_t so_saved_pcb;	
-u_int64_t cache_timestamp;	
 uint32_t so_eventmask;	
 pid_t last_pid;	
 u_int64_t last_upid;	

```
#### ipc_object

```diff

 struct ipc_object {
-_Atomic ipc_object_bits_t io_bits;	
-_Atomic ipc_object_refs_t io_references;	
+union {
+struct {
+ipc_object_type_t io_type;	
+ipc_object_state_t io_state;	
+uint8_t io_filtered;	
+uint8_t __io_unused1;	
+_Bool io_label_lock;	
+uint8_t __io_unused2;	
+}
+ ;	
+ipc_object_bits_t io_bits;	
+}
+ ;	
+os_ref_atomic_t io_references;	
+union {
+const void* iol_pointer;	
+unsigned long iol_value;	
+struct ipc_service_port_label* iol_service;	
+struct ipc_conn_port_label* iol_connection;	
+struct ipc_kobject_label* iol_kobject;	
+struct mk_timer* iol_mktimer;	
+}
+ ;	
 }

```
#### nxctl_traffic_rule_eth_storage

```c
struct nxctl_traffic_rule_eth_storage {
  struct nxctl_traffic_rule_eth_if_head res_if_list;
  uint32_t                              res_count;
}

```
#### sockaddr_inifscope

```c
struct sockaddr_inifscope {
  __uint8_t      sin_len;
  sa_family_t    sin_family;
  in_port_t      sin_port;
  struct in_addr sin_addr;
  union {
    char sin_zero[8];
    struct {
      __uint32_t ifscope;
    } _in_index;
  } un;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.130

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.130 {
-struct sockaddr* ptr;	
-struct sockaddr* ub;	
-struct sockaddr* lb;	
+struct flowadv* ptr;	
+struct flowadv* ub;	
+struct flowadv* lb;	
 }

```
#### ipc_port

```diff

 waitq_flags_t ip_tempowner;	
 waitq_flags_t ip_guarded;	
 waitq_flags_t ip_strict_guard;	
-waitq_flags_t ip_specialreply;	
 waitq_flags_t ip_sync_link_state;	
 waitq_flags_t ip_sync_bootstrap_checkin;	
-waitq_flags_t ip_immovable_receive;	
-waitq_flags_t ip_immovable_send;	
-waitq_flags_t ip_no_grant;	
 waitq_flags_t ip_tg_block_tracking;	
-waitq_flags_t ip_pinned;	
-waitq_flags_t ip_service_port;	
 waitq_flags_t ip_has_watchport;	
 waitq_flags_t ip_kernel_iotier_override;	
 waitq_flags_t ip_kernel_qos_override;	
-waitq_flags_t ip_reply_port_semantics;	
+waitq_flags_t ip_srp_lost_link;	
+waitq_flags_t ip_srp_msg_sent;	
+waitq_flags_t ip_bootstrap;	
+waitq_flags_t __ip_unused;	
 }
  ;	
 struct waitq ip_waitq;	

  ;	
 union {
 uintptr_t ip_kobject;	
+struct ipc_port* __ptrauth(DA, true, 0x2082) ip_nsrequest;	
+}
+ ;	
+union {
 ipc_importance_task_t ip_imp_task;	
 struct ipc_port* ip_sync_inheritor_port;	
 struct knote* ip_sync_inheritor_knote;	

 struct ipc_port* __ptrauth(DA, true, 0x78bc) ip_pdrequest;	
 }
  ;	
-struct ipc_port* ip_nsrequest;	
 ipc_port_request_table_t __ptrauth(DA, true, 0xb9dc) ip_requests;	
 struct turnstile* ip_send_turnstile;	
 mach_vm_address_t ip_context;	

 mach_port_mscount_t ip_mscount;	
 mach_port_rights_t ip_srights;	
 mach_port_rights_t ip_sorights;	
-union {
-ipc_kobject_label_t __ptrauth(DA, true, 0x71a0) ip_kolabel;	
-void* __ptrauth(DA, true, 0x306e) ip_splabel;	
-}
- ;	
 }

```
#### t8110dart_ppl

```diff

 struct t8110dart_ppl {
 struct ppl_iommu_state super;	
 uint64_t version;	
-t8110dart_dart_data darts[3];	
+t8110dart_dart_data darts[4];	
 t8110dart_sid_data* sids[256];	
 volatile uint32_t* ioaParentBase;	
 bitmap_t sidMask[4];	

 uint32_t diagLock;	
 uint32_t errCtrlOffset;	
 uint32_t numExceptRegs;	
+uint32_t maxSIDsInMismatch;	
 t8110dart_dart_hw_version hwVersion;	
 dart_id_t dart_id;	
 uint8_t power_state;	

 _Bool allowApfSidRemap;	
 _Bool ignoreSecondaryErrors;	
 _Bool inclusiveTzRange;	
+_Bool ignoreSIDCountMismatch;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.108

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.108 {
-struct __packet_opt* ptr;	
-struct __packet_opt* ub;	
-struct __packet_opt* lb;	
+struct mbuf* ptr;	
+struct mbuf* ub;	
+struct mbuf* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.79

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.79 {
-struct netif_queue* ptr;	
-struct netif_queue* ub;	
-struct netif_queue* lb;	
+struct __user_slot_desc* ptr;	
+struct __user_slot_desc* ub;	
+struct __user_slot_desc* lb;	
 }

```
#### __bounds_safety::wide_ptr.indexable.143

```c
struct __bounds_safety::wide_ptr.indexable.143 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.189

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.189 {
-struct pf_rulequeue* ptr;	
-struct pf_rulequeue* ub;	
-struct pf_rulequeue* lb;	
+struct flow_owner_bucket* ptr;	
+struct flow_owner_bucket* ub;	
+struct flow_owner_bucket* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.46

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.46 {
-struct nxdom* ptr;	
-struct nxdom* ub;	
-struct nxdom* lb;	
+struct __kern_packet* ptr;	
+struct __kern_packet* ub;	
+struct __kern_packet* lb;	
 }

```
#### lucid_context_version

```c
struct lucid_context_version {
  uint32_t version;
}

```
#### m_tag_type_entry

```diff

 struct m_tag_type_entry {
- struct m_tag* (u_int32_t, u_int16_t, uint16_t, int);* mt_alloc_func;	
- void (struct m_tag*);* mt_free_func;	
+m_tag_kalloc_func_t mt_alloc_func;	
+m_tag_kfree_func_t mt_free_func;	
 uint16_t mt_type;	
 uint16_t mt_len;	
 }

```
#### ifaddr

```diff

 struct ifaddr {
 lck_mtx_t ifa_lock;	
-os_ref_atomic_t ifa_refcnt;	
+os_refcnt_t ifa_refcnt;	
 uint32_t ifa_debug;	
 struct sockaddr* ifa_addr;	
 struct sockaddr* ifa_dstaddr;	

```
#### __bounds_safety::wide_ptr.bidi_indexable.232

```c
struct __bounds_safety::wide_ptr.bidi_indexable.232 {
  nstat_connection_descriptor *ptr;
  nstat_connection_descriptor *ub;
  nstat_connection_descriptor *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.47

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.47 {
-struct __quantum* ptr;	
-struct __quantum* ub;	
-struct __quantum* lb;	
+struct skmem_obj** ptr;	
+struct skmem_obj** ub;	
+struct skmem_obj** lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.183

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.183 {
-struct proc* ptr;	
-struct proc* ub;	
-struct proc* lb;	
+struct necp_kernel_ip_output_policy** ptr;	
+struct necp_kernel_ip_output_policy** ub;	
+struct necp_kernel_ip_output_policy** lb;	
 }

```
#### ipc_object_policy

```c
struct ipc_object_policy {
  const char       *pol_name;
  unsigned long     pol_kobject_stable;
  unsigned long     pol_kobject_permanent;
  ipc_move_policy_t pol_movability;
  unsigned long     pol_notif_port_destroy;
  unsigned long     pol_notif_no_senders;
  unsigned long     pol_notif_dead_name;
  unsigned long     pol_enforce_reply_semantics;
  unsigned long     pol_movable_send;
  const char       *pol_construct_entitlement;
  void(ipc_port_t, mach_port_mscount_t);
  *pol_kobject_no_senders;
  void(ipc_object_label_t);
  *pol_label_free;
}

```
#### __bounds_safety::wide_ptr.indexable.77

```diff

 struct __bounds_safety::wide_ptr.indexable.77 {
-void* ptr;	
-void* ub;	
+volatile struct ip* ptr;	
+volatile struct ip* ub;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.195

```c
struct __bounds_safety::wide_ptr.bidi_indexable.195 {
  struct __kern_buflet *ptr;
  struct __kern_buflet *ub;
  struct __kern_buflet *lb;
}

```
#### __bounds_safety::wide_ptr.indexable.91

```c
struct __bounds_safety::wide_ptr.indexable.91 {
  void *ptr;
  void *ub;
}

```
#### task_snapshot_v3

```c
struct task_snapshot_v3 {
  uint64_t ts_unique_pid;
  uint64_t ts_ss_flags;
  uint64_t ts_user_time_in_terminated_threads;
  uint64_t ts_system_time_in_terminated_threads;
  uint64_t ts_p_start_sec;
  uint64_t ts_task_size;
  uint64_t ts_max_resident_size;
  uint32_t ts_suspend_count;
  uint32_t ts_faults;
  uint32_t ts_pageins;
  uint32_t ts_cow_faults;
  uint32_t ts_was_throttled;
  uint32_t ts_did_throttle;
  uint32_t ts_latency_qos;
  int32_t  ts_pid;
  char     ts_p_comm[32];
  uint32_t ts_uid;
  uint32_t ts_gid;
}

```
#### __block_literal_15

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- IOReturn ();* __FuncPtr;	
-struct __block_descriptor_withcopydispose* __descriptor;	
-struct {
-void* __isa;	
-void* __forwarding;	
-int __flags;	
-int __size;	
-class OSObject* object;	
-}
-* object;	
-class IOService* provider;	
-const char* name;	
+ bool (class OSArray*);* __FuncPtr;	
+struct __block_descriptor* __descriptor;	
+IOPMDriverAssertionID assertionID;	
 }

```
#### net_aop_flow_stats

```c
struct net_aop_flow_stats {
  errno_t(void *, uint32_t, struct aop_flow_stats *);
  *fs_flow_stats;
  void *fs_prov_ctx;
}

```
#### IOCircularDataQueueMemory

```c
struct IOCircularDataQueueMemory {
  uint64_t sentinel;
  uint64_t _padding;
  union {
    volatile _Atomic __uint128_t queueStateVal;
    IOCircularDataQueueState     __queueState;
  };
  IOCircularDataQueueEntryHeader entries[1];
}

```
#### nstat_client

```diff

 lck_mtx_t ntc_user_mtx;	
 void* ntc_kctl;	
 u_int32_t ntc_unit;	
+u_int32_t ntc_client_id;	
 nstat_src_ref_t ntc_next_srcref;	
 tailq_head_nstat_src ntc_src_queue;	
 struct mbuf* ntc_accumulated;	

```
#### __bounds_safety::wide_ptr.bidi_indexable.33

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.33 {
-struct netif_stats* ptr;	
-struct netif_stats* ub;	
-struct netif_stats* lb;	
+struct __kern_packet* ptr;	
+struct __kern_packet* ub;	
+struct __kern_packet* lb;	
 }

```
#### flowq

```diff

 uint32_t fq_bytes;	
 int32_t fq_deficit;	
 fq_if_group_t* fq_group;	
-uint8_t fq_flags;	
+uint16_t fq_flags;	
+uint8_t fq_flowsrc;	
 uint8_t fq_sc_index;	
 _Bool fq_in_dqlist;	
 fq_tfc_type_t fq_tfc_type;	

 uint64_t fq_getqtime;	
 uint32_t fq_pkts_since_last_report;	
 uint64_t fq_next_tx_time;	
+uint32_t fq_congestion_cnt;	
+uint32_t fq_last_congestion_cnt;	
+codel_status_t codel_status;	
 union {
 uint64_t fq_updatetime;	
 uint64_t fq_empty_purge_time;	

```
#### __bounds_safety::wide_ptr.indexable.60

```c
struct __bounds_safety::wide_ptr.indexable.60 {
  char *ptr;
  char *ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.112

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.112 {
-struct __kern_channel_event_metadata* ptr;	
-struct __kern_channel_event_metadata* ub;	
-struct __kern_channel_event_metadata* lb;	
+struct flow_owner* ptr;	
+struct flow_owner* ub;	
+struct flow_owner* lb;	
 }

```
#### __block_literal_33

```diff

 int __reserved;	
  bool (const class OSSymbol*, class OSObject*);* __FuncPtr;	
 struct __block_descriptor* __descriptor;	
-class IOStateNotificationListener* listener;	
+class OSDictionary* result;	
 }

```
#### __bounds_safety::wide_ptr.indexable.218

```c
struct __bounds_safety::wide_ptr.indexable.218 {
  struct __bounds_safety::wide_ptr.indexable.42 * ptr;
  struct __bounds_safety::wide_ptr.indexable.42 * ub;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.44

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.44 {
-struct ifnet* ptr;	
-struct ifnet* ub;	
-struct ifnet* lb;	
+struct __kern_buflet* ptr;	
+struct __kern_buflet* ub;	
+struct __kern_buflet* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.132

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.132 {
-struct flow_route* ptr;	
-struct flow_route* ub;	
-struct flow_route* lb;	
+struct sk_stats_flow_owner* ptr;	
+struct sk_stats_flow_owner* ub;	
+struct sk_stats_flow_owner* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.63

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.63 {
-struct kern_pbufpool* ptr;	
-struct kern_pbufpool* ub;	
-struct kern_pbufpool* lb;	
+struct kern_nexus_provider* ptr;	
+struct kern_nexus_provider* ub;	
+struct kern_nexus_provider* lb;	
 }

```
#### memstat_cur_interval

```c
struct memstat_cur_interval {
  int64_t             num_procs;
  int64_t             num_notifs;
  int64_t             num_transitions;
  uint64_t            start_mt;
  _Atomic uint32_t    num_kills;
  vm_pressure_level_t max_level;
}

```
#### necp_client_flow_stats_index_header

```c
struct necp_client_flow_stats_index_header {
  struct necp_tlv_header stats_index_tlv_header;
  uint32_t               stats_index;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.17

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.17 {
-struct skmem_obj* ptr;	
-struct skmem_obj* ub;	
-struct skmem_obj* lb;	
+struct skmem_obj_info* ptr;	
+struct skmem_obj_info* ub;	
+struct skmem_obj_info* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.146

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.146 {
-struct kalloc_heap* ptr;	
-struct kalloc_heap* ub;	
-struct kalloc_heap* lb;	
+struct __kern_slot_desc* ptr;	
+struct __kern_slot_desc* ub;	
+struct __kern_slot_desc* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.165

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.165 {
-struct flow_mgr* ptr;	
-struct flow_mgr* ub;	
-struct flow_mgr* lb;	
+struct nx_qset_info* ptr;	
+struct nx_qset_info* ub;	
+struct nx_qset_info* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.0

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.0 {
-struct nxctl_traffic_rule_inet_if* ptr;	
-struct nxctl_traffic_rule_inet_if* ub;	
-struct nxctl_traffic_rule_inet_if* lb;	
+struct skmem_bufctl* ptr;	
+struct skmem_bufctl* ub;	
+struct skmem_bufctl* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.262

```c
struct __bounds_safety::wide_ptr.bidi_indexable.262 {
  struct traffic_stats *ptr;
  struct traffic_stats *ub;
  struct traffic_stats *lb;
}

```
#### _CEString

```c
struct _CEString {
  const uint8_t *data;
  size_t         length;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.31

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.31 {
-struct __kern_buflet* ptr;	
-struct __kern_buflet* ub;	
-struct __kern_buflet* lb;	
+struct skmem_region_params* ptr;	
+struct skmem_region_params* ub;	
+struct skmem_region_params* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.134

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.134 {
-struct __kern_packet** ptr;	
-struct __kern_packet** ub;	
-struct __kern_packet** lb;	
+struct ip* ptr;	
+struct ip* ub;	
+struct ip* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.40

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.40 {
-struct skmem_obj** ptr;	
-struct skmem_obj** ub;	
-struct skmem_obj** lb;	
+struct __kern_buflet* ptr;	
+struct __kern_buflet* ub;	
+struct __kern_buflet* lb;	
 }

```
#### net_aop_capab_proc_activity_bitmap

```c
struct net_aop_capab_proc_activity_bitmap {
  uint32_t kaopbm_version;
  void    *kaopbm_prov_ctx;
  errno_t(void *, struct aop_proc_activity_bitmap *, uint16_t *);
  *kaopbm_config;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.271

```c
struct __bounds_safety::wide_ptr.bidi_indexable.271 {
  struct necp_udp_stats *ptr;
  struct necp_udp_stats *ub;
  struct necp_udp_stats *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.57

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.57 {
-struct kalloc_type_view* ptr;	
-struct kalloc_type_view* ub;	
-struct kalloc_type_view* lb;	
+struct __packet_opt* ptr;	
+struct __packet_opt* ub;	
+struct __packet_opt* lb;	
 }

```
#### __bounds_safety::wide_ptr.indexable.42

```diff

 struct __bounds_safety::wide_ptr.indexable.42 {
-void* ptr;	
-void* ub;	
+struct sksegment_bkt* ptr;	
+struct sksegment_bkt* ub;	
 }

```
#### user32_package_ext_info

```c
struct user32_package_ext_info {
  user32_addr_t strings;
  uint32_t      num_entries;
  uint32_t      max_width;
}

```
#### vm_deferred_reclamation_metadata_s

```diff

 pid_t vdrm_pid;	
 vm_map_t vdrm_map;	
 os_refcnt_t vdrm_refcnt;	
-user_addr_t vdrm_buffer_addr;	
-mach_vm_size_t vdrm_buffer_size;	
+user_addr_t vdrm_ring_addr;	
+mach_vm_size_t vdrm_ring_size;	
 mach_vm_reclaim_count_t vdrm_buffer_len;	
 uint64_t vdrm_reclaimed_at;	
 uint32_t vdrm_waiters;	
 uint64_t vdrm_last_sample_abs;	
+size_t vdrm_kernel_bytes_reclaimed;	
+uint64_t vdrm_reclaimable_bytes_last;	
 uint64_t vdrm_reclaimable_bytes_wma;	
-size_t vdrm_reclaimable_bytes_min;	
-size_t vdrm_cumulative_uncancelled_bytes;	
-size_t vdrm_cumulative_reclaimed_bytes;	
 uint8_t vdrm_is_registered;	
 uint8_t __unused1;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.103

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.103 {
-struct nxprov_reg_ent* ptr;	
-struct nxprov_reg_ent* ub;	
-struct nxprov_reg_ent* lb;	
+struct sockaddr_in6* ptr;	
+struct sockaddr_in6* ub;	
+struct sockaddr_in6* lb;	
 }

```
#### __bounds_safety::wide_ptr.indexable.83

```c
struct __bounds_safety::wide_ptr.indexable.83 {
  uint8_t *ptr;
  uint8_t *ub;
}

```
#### _IOUCProcessToken

```c
struct _IOUCProcessToken {
  void  *token;
  UInt32 pid;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.26

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.26 {
-struct skmem_region_params* ptr;	
-struct skmem_region_params* ub;	
-struct skmem_region_params* lb;	
+void* ptr;	
+void* ub;	
+void* lb;	
 }

```
#### task_pend_token

```diff

 uint32_t tpt_update_tg_app_flag;	
 uint32_t tpt_update_game_mode;	
 uint32_t tpt_update_carplay_mode;	
+uint32_t tpt_update_appnap;	
 }
  ;	
 uint32_t tpt_value;	

```
#### __bounds_safety::wide_ptr.indexable.89

```diff

 struct __bounds_safety::wide_ptr.indexable.89 {
-void* ptr;	
-void* ub;	
+struct ip* ptr;	
+struct ip* ub;	
 }

```
#### aop_udp_stats

```c
struct aop_udp_stats {
  uint64_t _arr[8];
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.38

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.38 {
-struct __kern_quantum* ptr;	
-struct __kern_quantum* ub;	
-struct __kern_quantum* lb;	
+struct nxprov_params* ptr;	
+struct nxprov_params* ub;	
+struct nxprov_params* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.88

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.88 {
-struct kern_nexus_provider* ptr;	
-struct kern_nexus_provider* ub;	
-struct kern_nexus_provider* lb;	
+struct kern_channel* ptr;	
+struct kern_channel* ub;	
+struct kern_channel* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.68

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.68 {
-struct __kern_packet* ptr;	
-struct __kern_packet* ub;	
-struct __kern_packet* lb;	
+uint16_t* ptr;	
+uint16_t* ub;	
+uint16_t* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.110

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.110 {
-struct mit_cfg_tbl* ptr;	
-struct mit_cfg_tbl* ub;	
-struct mit_cfg_tbl* lb;	
+struct __kern_packet* ptr;	
+struct __kern_packet* ub;	
+struct __kern_packet* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.23

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.23 {
-struct netif_stats* ptr;	
-struct netif_stats* ub;	
-struct netif_stats* lb;	
+const struct nexus_adapter* ptr;	
+const struct nexus_adapter* ub;	
+const struct nexus_adapter* lb;	
 }

```
#### necp_route_rule

```diff

 u_int8_t constrained_action;	
 u_int8_t companion_action;	
 u_int8_t vpn_action;	
+u_int8_t ultra_constrained_action;	
 u_int exception_if_indices[10];	
 u_int8_t exception_if_actions[10];	
 os_refcnt_t refcount;	

```
#### aop_flow_stats

```c
struct aop_flow_stats {
  uint32_t          flow_id;
  uint32_t          reserved;
  uint64_t          rxbytes;
  uint64_t          txbytes;
  uint64_t          rxpkts;
  uint64_t          txpkts;
  aop_buffer_t      tx_buffer_stats;
  aop_buffer_t      rx_buffer_stats;
  activity_bitmap_t activity_bitmap;
  union {
    aop_tcp_info_t tcp_stats;
  } transport;
}

```
#### __bounds_safety::wide_ptr.indexable.183

```c
struct __bounds_safety::wide_ptr.indexable.183 {
  struct nstat_msg_sysinfo_counts *ptr;
  struct nstat_msg_sysinfo_counts *ub;
}

```
#### mbufq

```diff

 struct mbufq {
-struct mbuf* mq_first;	
-struct mbuf** mq_last;	
+struct counted_mbufq mq;	
+uint32_t count;	
+uint32_t bytes;	
 }

```
#### ntstat_sysinfo_keyval_iter

```c
struct ntstat_sysinfo_keyval_iter {
  uint32_t                             i;
  uint32_t                             nkeymax;
  __bounds_safety::counted_by::nkeymax kv;
}

```
#### __bounds_safety::wide_ptr.indexable.34

```diff

 struct __bounds_safety::wide_ptr.indexable.34 {
-struct skmem_bufctl* ptr;	
-struct skmem_bufctl* ub;	
+char* ptr;	
+char* ub;	
 }

```
#### __bounds_safety::wide_ptr.indexable.118

```c
struct __bounds_safety::wide_ptr.indexable.118 {
  struct fileglob **ptr;
  struct fileglob **ub;
}

```
#### utun_pcb

```diff

 struct ifnet* utun_ifp;	
 u_int32_t utun_unit;	
 u_int32_t utun_unique_id;	
-u_int32_t utun_flags;	
+u_int32_t utun_external_flags;	
+u_int32_t utun_internal_flags;	
 int utun_ext_ifdata_stats;	
 u_int32_t utun_max_pending_packets;	
 char utun_if_xname[24];	

 u_int32_t utun_pcb_drainers;	
 u_int32_t utun_pcb_data_path_state;	
 struct utun_nx utun_nx;	
-int utun_kpipe_enabled;	
-uuid_t utun_kpipe_uuid;	
-void* utun_kpipe_rxring;	
-void* utun_kpipe_txring;	
+u_int32_t utun_kpipe_count;	
+pid_t utun_kpipe_pid;	
+uuid_t utun_kpipe_uuid[4];	
+void* utun_kpipe_rxring[4];	
+void* utun_kpipe_txring[4];	
 struct kern_pbufpool* utun_kpipe_pp;	
 u_int32_t utun_kpipe_tx_ring_size;	
 u_int32_t utun_kpipe_rx_ring_size;	
+uuid_t utun_kpipe_proc_uuid;	
 struct kern_nexus* utun_netif_nexus;	
 struct kern_pbufpool* utun_netif_pp;	
-void* utun_netif_rxring;	
-void* utun_netif_txring;	
+void* utun_netif_rxring[1];	
+void* utun_netif_txring[4];	
 uint64_t utun_netif_txring_size;	
 u_int32_t utun_slot_size;	
 u_int32_t utun_netif_ring_size;	

```
#### fq_codel_classstats

```diff

 uint64_t fcls_ignore_tx_time;	
 uint64_t fcls_paced_pkts;	
 uint64_t fcls_fcl_pacing_needed;	
+uint64_t fcls_high_delay_drop;	
+uint64_t fcls_congestion_feedback;	
 }

```
#### in6_route_info_32

```c
struct in6_route_info_32 {
  struct in6_addr prefix;
  u_int8_t        prefixlen;
  u_short         defrtrs;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.177

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.177 {
-struct necp_route_rule* ptr;	
-struct necp_route_rule* ub;	
-struct necp_route_rule* lb;	
+struct necp_string_id_mapping* ptr;	
+struct necp_string_id_mapping* ub;	
+struct necp_string_id_mapping* lb;	
 }

```
#### __bounds_safety::wide_ptr.indexable.145

```c
struct __bounds_safety::wide_ptr.indexable.145 {
  void *ptr;
  void *ub;
}

```
#### nxctl_add_traffic_rule_eth_iocargs

```c
struct nxctl_add_traffic_rule_eth_iocargs {
  char                                   atre_ifname[16];
  struct ifnet_traffic_descriptor_eth    atre_td;
  struct ifnet_traffic_rule_action_steer atre_ra;
  uint32_t                               atre_flags;
  uuid_t                                 atre_uuid;
}

```
#### netif_agent_flow

```diff

 uuid_t naf_flow_uuid;	
 uuid_t naf_bind_key;	
 nexus_port_t naf_nx_port;	
-uint16_t naf_flags;	
+uint32_t naf_flags;	
 pid_t naf_pid;	
 union sockaddr_in_4_6 naf_daddr;	
 union sockaddr_in_4_6 naf_saddr;	

```
#### __bounds_safety::wide_ptr.bidi_indexable.187

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.187 {
-struct bridge_delayed_call* ptr;	
-struct bridge_delayed_call* ub;	
-struct bridge_delayed_call* lb;	
+struct flow_entry_dead* ptr;	
+struct flow_entry_dead* ub;	
+struct flow_entry_dead* lb;	
 }

```
#### nxctl_traffic_rule

```diff

 struct nxctl_traffic_rule {
-struct nxctl_traffic_rule_type* ntr_type;	
+uint8_t ntrt_type;	
 uint32_t ntr_flags;	
 os_refcnt_t ntr_refcnt;	
 uuid_t ntr_uuid;	

```
#### ledger_entry_info_v2

```c
struct ledger_entry_info_v2 {
  int64_t  lei_balance;
  int64_t  lei_credit;
  int64_t  lei_debit;
  uint64_t lei_limit;
  uint64_t lei_refill_period;
  uint64_t lei_last_refill;
  int64_t  lei_lifetime_max;
  uint64_t lei_reserved[4];
}

```
#### _CSConfigEnvironmentState

```diff

  _Bool ();* developerMode;	
  _Bool ();* demoMode;	
  _Bool ();* lockdownMode;	
+ _Bool ();* researchMode;	
+ _Bool ();* extendedResearchMode;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.69

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.69 {
-struct __kern_slot_desc* ptr;	
-struct __kern_slot_desc* ub;	
-struct __kern_slot_desc* lb;	
+struct __user_packet* ptr;	
+struct __user_packet* ub;	
+struct __user_packet* lb;	
 }

```
#### __bounds_safety::wide_ptr.indexable.90

```c
struct __bounds_safety::wide_ptr.indexable.90 {
  void *ptr;
  void *ub;
}

```
#### sptm_client_state

```diff

 unsigned int max_cpus;	
 const void* percpu_xnu_saved_state;	
 uint64_t feature_flags;	
-uint8_t reserved[136];	
+const void* allowed_io_frame_table;	
+unsigned int sptm_n_allowed_io_ranges;	
+const void* sptm_pmap_io_ranges;	
+unsigned int sptm_pmap_io_ranges_count;	
+uint8_t reserved[104];	
 }

```
#### __bounds_safety::wide_ptr.indexable.73

```diff

 struct __bounds_safety::wide_ptr.indexable.73 {
-void* ptr;	
-void* ub;	
+char* ptr;	
+char* ub;	
 }

```
#### fsw_stats

```diff

 struct fsw_stats {
-uint64_t _arr[119];	
+uint64_t _arr[126];	
 }

```
#### nstat_tu_shadow

```diff

 struct nstat_tu_shadow {
+nstat_locus shad_locus;	
 tailq_entry_tu_shadow shad_link;	
 userland_stats_request_vals_fn* shad_getvals_fn;	
 userland_stats_request_extension_fn* shad_get_extension_fn;	

```
#### __bounds_safety::wide_ptr.indexable.86

```diff

 struct __bounds_safety::wide_ptr.indexable.86 {
-void* ptr;	
-void* ub;	
+uint8_t* ptr;	
+uint8_t* ub;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.182

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.182 {
-struct kern_channel* ptr;	
-struct kern_channel* ub;	
-struct kern_channel* lb;	
+struct necp_flow_defunct* ptr;	
+struct necp_flow_defunct* ub;	
+struct necp_flow_defunct* lb;	
 }

```
#### processor_set

```diff

 lck_ticket_t sched_lock;	
 struct run_queue pset_runq;	
 struct rt_queue rt_runq;	
-uint64_t stealable_rt_threads_earliest_deadline;	
+_Atomic uint64_t stealable_rt_threads_earliest_deadline;	
 struct sched_clutch_root pset_clutch_root;	
 cpumap_t pending_AST_URGENT_cpu_mask;	
 cpumap_t pending_AST_PREEMPT_cpu_mask;	

 bitmap_t native_psets[1];	
 bitmap_t local_psets[1];	
 bitmap_t remote_psets[1];	
-sched_clutch_edge sched_edges[2];	
 pset_execution_time_t pset_execution_time[6];	
 uint64_t pset_cluster_shared_rsrc_load[2];	
+_Atomic sched_clutch_edge [6] sched_edges[2];	
+sched_pset_search_order_t spill_search_order[6];	
+uint8_t max_parallel_cores[6];	
+uint8_t max_parallel_clusters[6];	
+sched_clutch_edge sched_rt_edges[2];	
+sched_pset_search_order_t sched_rt_spill_search_order;	
+sched_pset_search_order_t sched_rt_steal_search_order;	
 cpumap_t perfcontrol_cpu_preferred_bitmask;	
 cpumap_t perfcontrol_cpu_migration_bitmask;	
 int cpu_preferred_last_chosen;	

```
#### __bounds_safety::wide_ptr.indexable.78

```diff

 struct __bounds_safety::wide_ptr.indexable.78 {
-char* ptr;	
-char* ub;	
+volatile struct ip6_hdr* ptr;	
+volatile struct ip6_hdr* ub;	
 }

```
#### nstat_generic_shadow

```diff

 struct nstat_generic_shadow {
+nstat_locus gshad_locus;	
 tailq_entry_generic_shadow gshad_link;	
 void* gshad_provider_context;	
 nstat_provider_request_vals_fn* gshad_getvals_fn;	

```
#### __bounds_safety::wide_ptr.bidi_indexable.138

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.138 {
-struct ifclassq* ptr;	
-struct ifclassq* ub;	
-struct ifclassq* lb;	
+const struct sadb_sa* ptr;	
+const struct sadb_sa* ub;	
+const struct sadb_sa* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.147

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.147 {
-nexus_channel_entry* ptr;	
-nexus_channel_entry* ub;	
-nexus_channel_entry* lb;	
+struct sk_stats_flow_adv_ent* ptr;	
+struct sk_stats_flow_adv_ent* ub;	
+struct sk_stats_flow_adv_ent* lb;	
 }

```
#### vm_map_entry

```diff

 unsigned long long no_cache;	
 unsigned long long vme_permanent;	
 unsigned long long superpage_size;	
-unsigned long long map_aligned;	
 unsigned long long zero_wired_pages;	
 unsigned long long used_for_jit;	
 unsigned long long csm_associated;	

```
#### nstat_msg_src_details

```c
struct nstat_msg_src_details {
  nstat_msg_hdr         hdr;
  nstat_src_ref_t       srcref;
  nstat_event_flags_t   event_flags;
  nstat_detailed_counts detailed_counts;
  nstat_provider_id_t   provider;
  u_int8_t              reserved[4];
  u_int8_t              data[0];
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.98

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.98 {
-struct flow_entry_dead* ptr;	
-struct flow_entry_dead* ub;	
-struct flow_entry_dead* lb;	
+struct __flow* ptr;	
+struct __flow* ub;	
+struct __flow* lb;	
 }

```
#### task_requested_policy

```diff

 uint64_t trp_sup_throughput;	
 uint64_t trp_sup_cpu;	
 uint64_t trp_sup_bg_sockets;	
+uint64_t trp_runaway_mitigation;	
 uint64_t trp_reserved;	
 }

```
#### necp_client_parsed_parameters

```diff

 u_int8_t demux_pattern_count;	
 uid_t uid;	
 uid_t persona_id;	
+u_int64_t extended_flags;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.71

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.71 {
-const char* ptr;	
-const char* ub;	
-const char* lb;	
+struct m_tag* ptr;	
+struct m_tag* ub;	
+struct m_tag* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.114

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.114 {
-struct xsockstat_n* ptr;	
-struct xsockstat_n* ub;	
-struct xsockstat_n* lb;	
+struct __kern_channel_event_metadata* ptr;	
+struct __kern_channel_event_metadata* ub;	
+struct __kern_channel_event_metadata* lb;	
 }

```
#### __bounds_safety::wide_ptr.indexable.31

```diff

 struct __bounds_safety::wide_ptr.indexable.31 {
-char* ptr;	
-char* ub;	
+struct skmem_bufctl_bkt* ptr;	
+struct skmem_bufctl_bkt* ub;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.102

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.102 {
-struct kern_pbufpool* ptr;	
-struct kern_pbufpool* ub;	
-struct kern_pbufpool* lb;	
+struct in6_addr* ptr;	
+struct in6_addr* ub;	
+struct in6_addr* lb;	
 }

```
#### ipc_space

```diff

 os_ref_atomic_t is_bits;	
 ipc_entry_num_t is_table_hashed;	
 ipc_entry_num_t is_table_free;	
+unsigned int is_entropy[1];	
+struct bool_gen is_prng;	
 struct {
 volatile ipc_entry_table_t __ptrauth(DA, true, 0xb8b5) __smr_ptr;	
 }
  is_table;	
 task_t __ptrauth(DA, true, 0xc547) is_task;	
+unsigned long is_policy;	
 thread_t is_grower;	
 ipc_label_t is_label;	
 ipc_entry_num_t is_low_mod;	
 ipc_entry_num_t is_high_mod;	
-struct bool_gen bool_gen;	
-unsigned int is_entropy[1];	
-int is_node_id;	
+_Atomic is_telemetry_t is_telemetry;	
 }

```
#### media_stats

```c
struct media_stats {
  traffic_stats_t ms_total;
  traffic_stats_t ms_cellular;
  traffic_stats_t ms_wifi_infra;
  traffic_stats_t ms_wifi_non_infra;
  traffic_stats_t ms_wired;
  traffic_stats_t ms_bluetooth;
  traffic_stats_t ms_alternate;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.30

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.30 {
-uint64_t* ptr;	
-uint64_t* ub;	
-uint64_t* lb;	
+struct ip* ptr;	
+struct ip* ub;	
+struct ip* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.142

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.142 {
-struct __kern_quantum* ptr;	
-struct __kern_quantum* ub;	
-struct __kern_quantum* lb;	
+const struct sadb_key* ptr;	
+const struct sadb_key* ub;	
+const struct sadb_key* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.194

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.194 {
-struct ip6_hdr* ptr;	
-struct ip6_hdr* ub;	
-struct ip6_hdr* lb;	
+struct ip* ptr;	
+struct ip* ub;	
+struct ip* lb;	
 }

```
#### IOService_StateNotificationItemCreate_Msg

```diff

 IORPCMessageMach mach;	
 mach_msg_port_descriptor_t __object__descriptor;	
 mach_msg_ool_descriptor_t itemName__descriptor;	
-mach_msg_ool_descriptor_t schema__descriptor;	
+mach_msg_ool_descriptor_t value__descriptor;	
 }

```
#### __block_literal_26

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- bool (class OSObject*);* __FuncPtr;	
+ void ();* __FuncPtr;	
 struct __block_descriptor* __descriptor;	
+class OSAction* action;	
 }

```
#### upl

```diff

 vm_offset_t kaddr;	
 vm_object_t map_object;	
 vector_upl_t vector_upl;	
+union {
 upl_t associated_upl;	
+struct upl_fs_verify_info* verify_info;	
+}
+ u_fs_un;	
 struct upl_io_completion* upl_iodone;	
 ppnum_t highest_page;	
 int upl_priority;	

```
#### __bounds_safety::wide_ptr.bidi_indexable.117

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.117 {
-struct sk_stats_flow* ptr;	
-struct sk_stats_flow* ub;	
-struct sk_stats_flow* lb;	
+struct __packet_opt* ptr;	
+struct __packet_opt* ub;	
+struct __packet_opt* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.197

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.197 {
-struct if_proto** ptr;	
-struct if_proto** ub;	
-struct if_proto** lb;	
+struct tcp_info* ptr;	
+struct tcp_info* ub;	
+struct tcp_info* lb;	
 }

```
#### _vector_upl

```diff

 uint32_t num_upls;	
 uint32_t invalid_upls;	
 uint32_t max_upls;	
-vm_map_t submap;	
-vm_offset_t submap_dst_addr;	
+vm_offset_t dst_addr;	
 vm_object_offset_t offset;	
 upl_page_info_array_t pagelist;	
 struct {

```
#### vm_page

```diff

 struct vm_page {
 union {
-vm_page_queue_chain_t vmp_q_pageq;	
-struct vm_page* vmp_q_snext;	
+vm_page_queue_chain_t vmp_pageq;	
+struct vm_page* vmp_snext;	
 }
- vmp_q_un;	
-vm_page_queue_chain_t vmp_listq;	
+ ;	
 vm_page_queue_chain_t vmp_specialq;	
-vm_object_offset_t vmp_offset;	
-vm_page_object_t vmp_object;	
-unsigned int vmp_wire_count;	
-unsigned int vmp_q_state;	
-unsigned int vmp_on_specialq;	
-unsigned int vmp_canonical;	
-unsigned int vmp_gobbled;	
-unsigned int vmp_laundry;	
-unsigned int vmp_no_cache;	
-unsigned int vmp_reference;	
-unsigned int vmp_lopage;	
-unsigned int vmp_realtime;	
-unsigned int vmp_unused_page_bits;	
+vm_page_queue_chain_t vmp_listq;	
 vm_page_packed_t vmp_next_m;	
+vm_page_object_t vmp_object;	
+vm_object_offset_t vmp_offset;	
+union {
+uint16_t vmp_wire_count;	
+uint16_t vmp_local_id;	
+}
+ ;	
+struct {
+vm_page_q_state_t vmp_q_state;	
+vm_page_specialq_t vmp_on_specialq;	
+uint8_t vmp_lopage;	
+uint8_t vmp_canonical;	
+}
+ ;	
+struct {
+uint8_t vmp_gobbled;	
+uint8_t vmp_laundry;	
+uint8_t vmp_no_cache;	
+uint8_t vmp_reference;	
+uint8_t vmp_realtime;	
+uint8_t __vmp_reserved1;	
+uint8_t __vmp_reserved2;	
+uint8_t __vmp_reserved3;	
+}
+ ;	
 unsigned int vmp_busy;	
 unsigned int vmp_wanted;	
 unsigned int vmp_tabled;	

```
#### __bounds_safety::wide_ptr.bidi_indexable.144

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.144 {
-lck_mtx_t* ptr;	
-lck_mtx_t* ub;	
-lck_mtx_t* lb;	
+struct in6_ifaddr* ptr;	
+struct in6_ifaddr* ub;	
+struct in6_ifaddr* lb;	
 }

```
#### __bounds_safety::wide_ptr.indexable.182

```c
struct __bounds_safety::wide_ptr.indexable.182 {
  struct nstat_sysinfo_keyval *ptr;
  struct nstat_sysinfo_keyval *ub;
}

```
#### arm_guest_amx_context

```c
struct arm_guest_amx_context {
  uint8_t[64] x[8];
  uint8_t[64] y[8];
  uint8_t[64] z[64];
  uint64_t amx_state_t_el1;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.73

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.73 {
-struct __slot_desc* ptr;	
-struct __slot_desc* ub;	
-struct __slot_desc* lb;	
+const struct __kern_packet** ptr;	
+const struct __kern_packet** ub;	
+const struct __kern_packet** lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.54

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.54 {
-struct __packet_opt* ptr;	
-struct __packet_opt* ub;	
-struct __packet_opt* lb;	
+struct mbuf* ptr;	
+struct mbuf* ub;	
+struct mbuf* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.90

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.90 {
-struct __flow* ptr;	
-struct __flow* ub;	
-struct __flow* lb;	
+struct __kern_slot_desc* ptr;	
+struct __kern_slot_desc* ub;	
+struct __kern_slot_desc* lb;	
 }

```
#### necp_client_nexus_parameters

```diff

 unsigned int no_wake_from_sleep;	
 unsigned int is_demuxable_parent;	
 unsigned int reuse_port;	
+unsigned int use_aop_offload;	
 uuid_t parent_flow_uuid;	
 struct necp_demux_pattern demux_patterns[4];	
 uint8_t demux_pattern_count;	

```
#### __bounds_safety::wide_ptr.bidi_indexable.89

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.89 {
-const struct __kern_buflet* ptr;	
-const struct __kern_buflet* ub;	
-const struct __kern_buflet* lb;	
+struct __kern_buflet_ext* ptr;	
+struct __kern_buflet_ext* ub;	
+struct __kern_buflet_ext* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.159

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.159 {
-struct nx_qset_info* ptr;	
-struct nx_qset_info* ub;	
-struct nx_qset_info* lb;	
+struct sastat* ptr;	
+struct sastat* ub;	
+struct sastat* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.16

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.16 {
-struct _slot* ptr;	
-struct _slot* ub;	
-struct _slot* lb;	
+class_queue_t* ptr;	
+class_queue_t* ub;	
+class_queue_t* lb;	
 }

```
#### nx_flow_req

```diff

 union sockaddr_in_4_6 nfr_daddr;	
 uint8_t nfr_ip_protocol;	
 uint8_t nfr_transport_protocol;	
-uint16_t nfr_flags;	
+uint32_t nfr_flags;	
 uuid_t nfr_flow_uuid;	
 packet_svc_class_t nfr_svc_class;	
 uuid_t nfr_euuid;	

 uuid_t nfr_parent_flow_uuid;	
 uint8_t nfr_flow_demux_count;	
 struct flow_demux_pattern nfr_flow_demux_patterns[4];	
+uint32_t nfr_flowid;	
 union {
 struct {
 char _nfr_kernel_field_start[0];	

```
#### mptcp_add_addr_opt

```diff

 uint8_t maddr_flags;	
 uint8_t maddr_subtype;	
 uint8_t maddr_addrid;	
-union {
-struct {
-struct in_addr maddr_addrv4;	
-uint32_t maddr_pad[3];	
-}
- ;	
-struct {
-struct in6_addr maddr_addrv6;	
-}
- ;	
-}
- maddr_u;	
 }

```
#### rt_msghdr_prelude

```c
struct rt_msghdr_prelude {
  u_short rtm_msglen;
}

```
#### _CEIterateArgs

```c
struct _CEIterateArgs {
  void      *userData;
  size_t     index;
  size_t     count;
  _Bool      stopIteration;
  CEReturn_t __V2Return;
}

```
#### IOCircularDataQueue

```c
struct IOCircularDataQueue {
  IOCircularDataQueueMemoryCursor queueCursor;
  IOCircularDataQueueMemory      *__ptrauth(DA, true, 0xaa79) queueMemory;
  IOCircularDataQueueDescription  queueHeaderShadow;
  class IOBufferMemoryDescriptor *__ptrauth(DA, true, 0x65d0) iomd;
}

```
#### vm_statistics64

```diff

 natural_t external_page_count;	
 natural_t internal_page_count;	
 uint64_t total_uncompressed_pages_in_compressor;	
+uint64_t swapped_count;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.129

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.129 {
-struct ip* ptr;	
-struct ip* ub;	
-struct ip* lb;	
+struct tseg_qent* ptr;	
+struct tseg_qent* ub;	
+struct tseg_qent* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.85

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.85 {
-struct nexus_adapter* ptr;	
-struct nexus_adapter* ub;	
-struct nexus_adapter* lb;	
+struct nxdom* ptr;	
+struct nxdom* ub;	
+struct nxdom* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.67

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.67 {
-struct __packet_opt* ptr;	
-struct __packet_opt* ub;	
-struct __packet_opt* lb;	
+struct __user_quantum* ptr;	
+struct __user_quantum* ub;	
+struct __user_quantum* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.168

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.168 {
-struct flow_owner_bucket* ptr;	
-struct flow_owner_bucket* ub;	
-struct flow_owner_bucket* lb;	
+struct netif_qstats_info* ptr;	
+struct netif_qstats_info* ub;	
+struct netif_qstats_info* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.99

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.99 {
-struct ifnet* ptr;	
-struct ifnet* ub;	
-struct ifnet* lb;	
+union sockaddr_in_4_6* ptr;	
+union sockaddr_in_4_6* ub;	
+union sockaddr_in_4_6* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.224

```c
struct __bounds_safety::wide_ptr.bidi_indexable.224 {
  struct necp_domain_trie *ptr;
  struct necp_domain_trie *ub;
  struct necp_domain_trie *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.199

```c
struct __bounds_safety::wide_ptr.bidi_indexable.199 {
  struct sk_stats_flow *ptr;
  struct sk_stats_flow *ub;
  struct sk_stats_flow *lb;
}

```
#### psemstats

```diff

 struct psemstats {
-long goodhits;	
-long neghits;	
-long badhits;	
-long falsehits;	
-long miss;	
-long longnames;	
+long pstats_hits;	
+long pstats_miss;	
+long pstats_local_hits;	
+long pstats_global_hits;	
+long pstats_local_miss;	
+long pstats_global_miss;	
+long pstats_local_collisions;	
+long pstats_global_collisions;	
+long pstats_fallback_hits;	
+long pstats_fallback_miss;	
+long pstats_neghits;	
+long pstats_longnames;	
 }

```
#### utun_detached_channels

```c
struct utun_detached_channels {
  int                   count;
  struct kern_pbufpool *pp;
  uuid_t                uuids[4];
}

```
#### nxdom

```diff

  boolean_t (struct kern_nexus*, nexus_port_t);* nxdom_port_is_reserved;	
  int (struct kern_nexus*, nexus_port_t*, struct nxbind*, void*);* nxdom_bind_port;	
  int (struct kern_nexus*, nexus_port_t);* nxdom_unbind_port;	
- int (struct kern_nexus_domain_provider*, struct kern_nexus*, struct kern_channel*, struct chreq*, struct kern_channel*, struct nxbind*, struct proc*);* nxdom_connect;	
+ int (struct kern_nexus_domain_provider*, struct kern_nexus*, struct kern_channel*, struct chreq*, struct nxbind*, struct proc*);* nxdom_connect;	
  void (struct kern_nexus_domain_provider*, struct kern_nexus*, struct kern_channel*);* nxdom_disconnect;	
  void (struct kern_nexus_domain_provider*, struct kern_nexus*, struct kern_channel*, struct proc*);* nxdom_defunct;	
  void (struct kern_nexus_domain_provider*, struct kern_nexus*, struct kern_channel*, boolean_t);* nxdom_defunct_finalize;	

```
#### pset_node

```diff

 struct pset_node {
 processor_set_t psets;	
-pset_node_t nodes;	
 pset_node_t node_list;	
 pset_cluster_type_t pset_cluster_type;	
 pset_map_t pset_map;	

```
#### _SIPHASH_CTX

```c
struct _SIPHASH_CTX {
  uint64_t v[4];
  union {
    uint64_t b64;
    uint8_t  b8[8];
  } buf;
  uint64_t bytes;
  uint8_t  buflen;
  uint8_t  rounds_compr;
  uint8_t  rounds_final;
  uint8_t  initialized;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.272

```c
struct __bounds_safety::wide_ptr.bidi_indexable.272 {
  nstat_udp_descriptor *ptr;
  nstat_udp_descriptor *ub;
  nstat_udp_descriptor *lb;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.180

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.180 {
-struct necp_kernel_ip_output_policy** ptr;	
-struct necp_kernel_ip_output_policy** ub;	
-struct necp_kernel_ip_output_policy** lb;	
+struct ucred* ptr;	
+struct ucred* ub;	
+struct ucred* lb;	
 }

```
#### __block_literal_31

```diff

 void* __isa;	
 int __flags;	
 int __reserved;	
- bool (class OSObject*);* __FuncPtr;	
+ void ();* __FuncPtr;	
 struct __block_descriptor* __descriptor;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.119

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.119 {
-struct nx_flowswitch* ptr;	
-struct nx_flowswitch* ub;	
-struct nx_flowswitch* lb;	
+struct sk_stats_flow_switch* ptr;	
+struct sk_stats_flow_switch* ub;	
+struct sk_stats_flow_switch* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.105

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.105 {
-struct ifaddr* ptr;	
-struct ifaddr* ub;	
-struct ifaddr* lb;	
+struct counted_mbufq* ptr;	
+struct counted_mbufq* ub;	
+struct counted_mbufq* lb;	
 }

```
#### tcpopt

```diff

 uint32_t to_tsval;	
 uint32_t to_tsecr;	
 uint16_t to_mss;	
-uint8_t to_requested_s_scale;	
+uint8_t to_wscale;	
 uint8_t to_nsacks;	
 __bounds_safety::sized_by::to_sacks_size to_sacks;	
 uint32_t to_sacks_size;	

```
#### __bounds_safety::wide_ptr.indexable.51

```diff

 struct __bounds_safety::wide_ptr.indexable.51 {
-volatile struct ip6_hdr* ptr;	
-volatile struct ip6_hdr* ub;	
+char* ptr;	
+char* ub;	
 }

```
#### net_aop_capab_stats

```c
struct net_aop_capab_stats {
  uint32_t kaopcgs_version;
  void    *kaopcgs_prov_ctx;
  errno_t(void *, net_aop_stats_type_t, uint8_t *, size_t);
  *kaopcgs_config;
}

```
#### __bounds_safety::wide_ptr.bidi_indexable.181

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.181 {
-channel_ring_stats* ptr;	
-channel_ring_stats* ub;	
-channel_ring_stats* lb;	
+nstat_msg_sysinfo_counts* ptr;	
+nstat_msg_sysinfo_counts* ub;	
+nstat_msg_sysinfo_counts* lb;	
 }

```
#### __bounds_safety::wide_ptr.indexable.114

```diff

 struct __bounds_safety::wide_ptr.indexable.114 {
-char* ptr;	
-char* ub;	
+void* ptr;	
+void* ub;	
 }

```
#### rtentry

```diff

 u_int32_t rtt_min;	
 u_int32_t rtt_expire_ts;	
 u_int8_t rtt_index;	
+uint64_t rt_qset_id;	
+uint32_t rt_tr_genid;	
 struct eventhandler_lists_ctxt rt_evhdlr_ctxt;	
 }

```
#### workq_aio_s

```c
struct workq_aio_s {
  thread_call_t                 wa_death_call;
  struct workq_aio_uthread_head wa_thrunlist;
  struct workq_aio_uthread_head wa_thidlelist;
  struct {
    struct aio_workq_entry  *tqh_first;
    struct aio_workq_entry **tqh_last;
  } wa_aioq_entries;
  proc_t                      wa_proc;
  _Atomic workq_state_flags_t wa_flags;
  uint16_t                    wa_nthreads;
  uint16_t                    wa_thidlecount;
  uint16_t                    wa_thdying_count;
}

```
#### sched_clutch_bucket_group

```diff

 _Atomic uint32_t scbg_timeshare_tick;	
 _Atomic uint32_t scbg_pri_shift;	
 _Atomic uint32_t scbg_preferred_cluster;	
-uint32_t scbg_amp_rebalance_last_chosen;	
 struct sched_clutch* scbg_clutch;	
 sched_clutch_counter_time_t scbg_blocked_data;	
 sched_clutch_counter_time_t scbg_pending_data;	

```
#### __bounds_safety::wide_ptr.bidi_indexable.176

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.176 {
-struct kern_event_msg* ptr;	
-struct kern_event_msg* ub;	
-struct kern_event_msg* lb;	
+nstat_ifnet_desc_link_status* ptr;	
+nstat_ifnet_desc_link_status* ub;	
+nstat_ifnet_desc_link_status* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.166

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.166 {
-struct flow_entry_dead* ptr;	
-struct flow_entry_dead* ub;	
-struct flow_entry_dead* lb;	
+struct tcphdr* ptr;	
+struct tcphdr* ub;	
+struct tcphdr* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.94

```diff

 struct __bounds_safety::wide_ptr.bidi_indexable.94 {
-struct netif_queue* ptr;	
-struct netif_queue* ub;	
-struct netif_queue* lb;	
+struct kern_pbufpool_u_bft_bkt* ptr;	
+struct kern_pbufpool_u_bft_bkt* ub;	
+struct kern_pbufpool_u_bft_bkt* lb;	
 }

```
#### __bounds_safety::wide_ptr.bidi_indexable.205

```c
struct __bounds_safety::wide_ptr.bidi_indexable.205 {
  struct _services *ptr;
  struct _services *ub;
  struct _services *lb;
}

```
