# Import necessary libraries
from Crypto.PublicKey import RSA
from Crypto.Util.number import inverse

# Given data
n = 20275725101473426999610084123020248290129213926585084438752915204909581424818836798673019110617556014803726965616338885453492666351217215034931790256712756086561821632690687205196237137887228270928509776194528276136684350927672479580167472118982603182912850770807723377902174289662158049033927156727452430230013153698667105803226656736552135913318475343399101814434226788644339297838517639643195185914616827198056693934557514165978081656301990789103328835595780784126740096138982740676641953850405587535290337004397973547242480930369322199503040459329186640740198978689871723598586177026481471318777599135524282869761
c = 7556779587415034698376883742370217095882021125474092151338802626835907964914948187780980857013197065084371111263694652539331100536190031701079440606454962110268315016600075419403137462594068246518448136445545699028611850512632052679552204368131011052863503254762342971639805183112191728060755991482413688428279355129202793351857407160109820018994563845456287858067497842980630864710055105771421677112780935076470622127456186401201370223576833437441177947703383057918053676606435366442804346513494040688810584589324477694176872865662719930211569130061277868100253973780270487932673530450905129282071834907093478028040
e = 65537
p = 125134920897549739255174050341300713003231661235612680264588621981385509131151600441745010195461041895934604306296201492565968578872268838578738413968550730995589164636193457091841895757037495023347713684830455177226592265814480360704148656189916226253157503713016954411923066833839400357410487044937109498707
q = 162030909965360796242343215135512737840926678817313914224913003548743640643247949784642193150161095933868767005955222826671030639705063451935787818921075449976527699144993027602615001124674355917780757694012526167683482071075831309533193962594992252249357997031610675138835102793281746914804337797305703778523

# Compute phi(n)
phi = (p - 1) * (q - 1)

# Compute d
d = inverse(e, phi)

# Decrypt the message
m = pow(c, d, n)

# Convert the decrypted message to bytes and then to string
decrypted_message = m.to_bytes((m.bit_length() + 7) // 8, byteorder='big').decode('utf-8')

print(decrypted_message)
