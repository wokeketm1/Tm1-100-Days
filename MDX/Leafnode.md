
請替換**sDimension** **sConsolidate**


Method1:
{TM1FILTERBYLEVEL({DESCENDANTS([   **sDimension**  ].[ **sConsolidate** ]) }, 0)}

Method2:
{TM1FILTERBYLEVEL( {TM1DRILLDOWNMEMBER( {[   **sDimension**  ].[ **sConsolidate** ]}, ALL, RECURSIVE )}, 0)}
