## KDKs

- `KDK_15.1_24B5046f.kdk/System/Library/Kernels/kernel.release.t6030`
- `KDK_15.1_24B5055e.kdk/System/Library/Kernels/kernel.release.t6030`

#### _TrustCache

```diff

 struct _TrustCache {
 struct _TrustCache* next;	
-struct _TrustCache* prev;	
 TCType_t type;	
 size_t moduleSize;	
 const TrustCacheModuleBase_t* module;	

```
#### cfil_crypto_data

```diff

 u_int32_t socketProtocol;	
 pid_t pid;	
 pid_t effective_pid;	
+pid_t responsible_pid;	
 uuid_t uuid;	
 uuid_t effective_uuid;	
+uuid_t responsible_uuid;	
 u_int64_t byte_count_in;	
 u_int64_t byte_count_out;	
 }

```
#### cfil_opt_sock_info

```diff

 union sockaddr_in_4_6 cfs_remote;	
 pid_t cfs_pid;	
 pid_t cfs_e_pid;	
+pid_t cfs_r_pid;	
 uuid_t cfs_uuid;	
 uuid_t cfs_e_uuid;	
+uuid_t cfs_r_uuid;	
 }

```
#### cfil_msg_sock_attached

```diff

 int cfs_unused;	
 pid_t cfs_pid;	
 pid_t cfs_e_pid;	
+pid_t cfs_r_pid;	
 uuid_t cfs_uuid;	
 uuid_t cfs_e_uuid;	
+uuid_t cfs_r_uuid;	
 union sockaddr_in_4_6 cfs_src;	
 union sockaddr_in_4_6 cfs_dst;	
 int cfs_conn_dir;	

```
