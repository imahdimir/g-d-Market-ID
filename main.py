##


from githubdata import GithubData
from mirutil.df_utils import save_df_as_a_nice_xl as sxl
from mirutil.df_utils import read_data_according_to_type as rdata


rp_url = 'https://github.com/imahdimir/d-Final-Markets-ID'

mktid = 'MarketId'
name = 'Name'

def main() :
  pass

  ##

  rp = GithubData(rp_url)
  rp.clone()
  ##
  fpn = rp.data_filepath
  df = rdata(fpn)
  ##
  df = df[[mktid, name]]
  ##
  df = df.sort_values([mktid, name])
  ##
  df = df.drop_duplicates(subset = mktid)
  ##
  sxl(df , fpn)
  ##
  cur_module_repo = 'https://github.com/' + rp.usr + '/' + 'gov-'+ rp.repo_name
  ##
  commit_msg = 'checked'
  commit_msg += f' by repo: {cur_module_repo}'

  rp.commit_push(commit_msg)
  ##


  rp.rmdir()

  ##


##

##